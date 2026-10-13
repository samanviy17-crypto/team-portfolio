"""Capture tested PNEC UI states using only disposable synthetic data.
Uses the built frontend (preview on 4500) and an isolated file SQLite backend.
Screenshots/logs are local until explicitly approved for publication. This is
AI-assisted verification of shared code, not anyone's personal Create evidence.
"""
import json
import secrets
import sys
import tempfile
import threading
from datetime import datetime, timedelta, timezone
from pathlib import Path
from playwright.sync_api import sync_playwright, expect
from werkzeug.serving import make_server, WSGIRequestHandler

ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / 'docs/pnec-sprint3/2026-10-13'
sys.path.insert(0, str(ROOT / 'Beasts_Flask'))
from app.config import Config
from app import create_app, db
from app.models.user import User
from app.models.neighborhood import Neighborhood
from app.models.operations import VolunteerTask, HouseholdPreparedness
from app.services import risk_service

class QuietHandler(WSGIRequestHandler):
    def log_request(self, *args, **kwargs): pass

with tempfile.TemporaryDirectory(prefix='pnec-sprint3-') as directory:
    Config.SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(Path(directory) / 'synthetic.db')
    Config.ADMIN_PASSWORD = ''
    Config.SECRET_KEY = secrets.token_hex(32)
    Config.GROQ_API_KEY = Config.GEMINI_API_KEY = Config.GITHUB_TOKEN = None
    risk_service.get_risk_assessment = lambda *args, **kwargs: {
        'fire_level':'LOW', 'flood_level':'LOW', 'heat_level':'LOW',
        'fire_score':1, 'flood_score':1, 'heat_score':1, 'is_stale':False}
    app = create_app()
    app.config.update(TESTING=True, SESSION_COOKIE_SECURE=False)
    accounts = {}
    with app.app_context():
        nid = Neighborhood.query.first().id
        for key, role in [('resident','resident'), ('coordinator','coordinator'), ('other','resident')]:
            u = User(email=key+'@example.test', display_name='Synthetic '+key,
                     password_hash='not-for-login', role=role, neighborhood_id=nid)
            u.generate_token(); db.session.add(u); db.session.flush()
            accounts[key] = {'token':u.auth_token, 'user':u.to_dict()}
        db.session.add(VolunteerTask(title='Synthetic preparedness training',
            description='Synthetic test shift, not a real PNEC event',
            neighborhood_id=nid, starts_at=datetime.now(timezone.utc).replace(tzinfo=None)+timedelta(days=2),
            capacity=1, created_by=accounts['coordinator']['user']['id']))
        db.session.commit()
    backend = make_server('127.0.0.1',0,app,request_handler=QuietHandler)
    thread = threading.Thread(target=backend.serve_forever,daemon=True); thread.start()
    cases=[]; images=[]
    def record(name, expected, actual):
        cases.append({'scenario':name,'expected':expected,'actual':actual,'status':'PASS'})
        print('PASS: '+name,flush=True)
    try:
        with sync_playwright() as play:
            browser=play.chromium.launch()
            def account(key=None):
                context=browser.new_context(viewport={'width':1280,'height':1000})
                context.route('**/*',lambda route: route.continue_() if route.request.url.startswith(('http://127.0.0.1','http://localhost')) else route.abort())
                context.route('http://127.0.0.1:8425/**',lambda route: route.continue_(url=route.request.url.replace(':8425', ':'+str(backend.server_port),1)))
                if key:
                    data=accounts[key]
                    context.add_init_script('localStorage.setItem("pnec_token",'+json.dumps(data['token'])+'); localStorage.setItem("pnec_user",'+json.dumps(json.dumps(data['user']))+');')
                return context,context.new_page()
            context,page=account('resident')
            area=lambda title:page.locator('.community-tools section').filter(has=page.get_by_role('heading',name=title,exact=True)).last
            def capture(locator,name,caption):
                path=EVIDENCE/'screenshots'/name
                locator.screenshot(path=str(path))
                images.append({'path':'screenshots/'+name,'caption':caption})
            page.goto('http://127.0.0.1:4500/pages/checklist.html',wait_until='domcontentloaded')
            expect(page.locator('#kit-sync-status')).to_have_text('Saved to your account.')
            quiz=area('Preparedness assessment')
            expect(quiz.locator('select')).to_have_count(10)
            capture(quiz,'quiz-interface.png','Ten-question quiz before answering, synthetic authenticated resident.')
            for count in [0,5,10]:
                for index,choice in enumerate(quiz.locator('select').all()): choice.select_option('yes' if index<count else 'no')
                quiz.get_by_role('button',name='Save assessment',exact=True).click()
                expect(quiz.get_by_role('status').first).to_contain_text(f'{count*10}%')
                if count==10: expect(quiz.get_by_role('status').first).to_contain_text('practice your plan')
                else: expect(quiz.get_by_role('status').first).to_contain_text('Review')
                capture(quiz,f'quiz-{count}-of-10.png',f'Actual API result {count}/10 = {count*10}%, with returned recommendation text.')
                record(f'Quiz {count}/10',f'{count*10}% and corresponding recommendations',quiz.get_by_role('status').first.inner_text())
            page.locator('#cb-water').check()
            expect(page.locator('#kit-sync-status')).to_have_text('Saved to your account.')
            page.reload(wait_until='domcontentloaded')
            expect(page.locator('#kit-sync-status')).to_have_text('Saved to your account.')
            expect(page.locator('#cb-water')).to_be_checked()
            with app.app_context():
                assert db.session.get(HouseholdPreparedness,accounts['resident']['user']['id']).items['water'] is True
            capture(page.locator('.checklist-page'),'checklist-persisted.png','Water remains checked after reload; isolated database value verified true.')
            record('Checklist persistence','Checked UI and database true after reload','Both verified true')

            def html_failure(route): route.fulfill(status=502,content_type='text/html',body='<html>synthetic upstream failure</html>')
            page.route('**/api/preparedness',html_failure)
            page.locator('#cb-water').uncheck()
            expect(page.locator('#kit-sync-status')).to_contain_text('Account save failed')
            expect(page.locator('#kit-sync-status')).to_contain_text('unexpected error')
            capture(page.locator('.checklist-page'),'checklist-server-error.png','Simulated HTML 502: useful error shown and unchecked water retained locally; not a production incident.')
            record('Checklist HTML 502','Safe server error with pending edits','Safe error displayed; unsaved water=false retained')
            page.unroute('**/api/preparedness',html_failure)
            def offline(route): route.abort()
            page.route('**/api/preparedness',offline)
            page.reload(wait_until='domcontentloaded')
            expect(page.locator('#kit-sync-status')).to_contain_text('Account checklist unavailable')
            expect(page.locator('#cb-water')).not_to_be_checked()
            capture(page.locator('.checklist-page'),'checklist-offline-pending.png','Simulated disconnected preparedness API after reload; pending water=false survives.')
            record('Offline reload','Pending edit retained and connection feedback','Water unchecked with unavailable API message')
            page.unroute('**/api/preparedness',offline)
            page.evaluate('pnecRetryKit()')
            expect(page.locator('#kit-sync-status')).to_have_text('Saved to your account.')
            with app.app_context():
                assert db.session.get(HouseholdPreparedness,accounts['resident']['user']['id']).items['water'] is False
            capture(page.locator('.checklist-page'),'checklist-recovered.png','Explicit Retry account save succeeds; isolated database now water=false.')
            record('Explicit retry recovery','Pending changes persisted without loss','UI saved and database water=false')

            page.goto('http://127.0.0.1:4500/pages/profile.html',wait_until='domcontentloaded')
            expect(page.locator('#edit-display-name')).to_have_value('Synthetic resident')
            page.locator('#edit-display-name').fill('Synthetic retained draft')
            page.route('**/api/auth/profile',html_failure)
            page.locator('#profile-save-btn').click()
            expect(page.locator('#profile-error')).to_be_visible()
            expect(page.locator('#profile-save-btn')).to_be_enabled()
            expect(page.locator('#edit-display-name')).to_have_value('Synthetic retained draft')
            capture(page.locator('.profile-edit-section').last,'profile-failed-save-draft.png','Simulated profile HTML 502 preserves the current form draft and re-enables Save.')
            record('Profile failed save','Draft remains; retry enabled','Retained synthetic draft and enabled Save verified')
            page.unroute('**/api/auth/profile',html_failure)
            page.locator('#profile-save-btn').click()
            expect(page.locator('#profile-success')).to_be_visible()
            page.reload(wait_until='domcontentloaded')
            expect(page.locator('#edit-display-name')).to_have_value('Synthetic retained draft')
            record('Profile retry and reload','Successful update persists','Synthetic retained draft loaded after reload')

            page.goto('http://127.0.0.1:4500/pages/volunteer.html',wait_until='domcontentloaded')
            shifts=area('Volunteer shifts and tasks')
            expect(shifts.get_by_role('button',name='Claim a slot',exact=True)).to_be_visible()
            capture(shifts,'volunteer-available.png','Existing shared volunteer UI: synthetic shift has 0/1 slots claimed.')
            shifts.get_by_role('button',name='Claim a slot',exact=True).click()
            expect(shifts.get_by_role('button',name='Cancel my signup',exact=True)).to_be_visible()
            expect(shifts).to_contain_text('1/1 slots claimed')
            capture(shifts,'volunteer-signed-up.png','Existing shared signup behavior: synthetic resident claims the single slot.')
            shifts.get_by_role('button',name='Cancel my signup',exact=True).click()
            expect(shifts.get_by_role('button',name='Claim a slot',exact=True)).to_be_visible()
            expect(shifts).to_contain_text('0/1 slots claimed')
            capture(shifts,'volunteer-cancelled.png','Existing shared cancellation behavior restores availability; no new Joan implementation.')
            record('Shared signup/cancellation smoke','Capacity 0 → 1 → 0','UI claim/cancel and counts verified; concurrency not tested')

            page.goto('http://127.0.0.1:4500/pages/checklist.html',wait_until='domcontentloaded')
            hazard=area('Report a neighborhood hazard')
            hazard.get_by_label('Neighborhood',exact=True).select_option(str(nid))
            hazard.get_by_label('Hazard type').select_option('route')
            hazard.get_by_label('Location',exact=True).fill('Synthetic test location')
            hazard.get_by_label('Description',exact=True).fill('Synthetic report for isolated verification, not a real hazard')
            hazard.get_by_role('button',name='Submit hazard report',exact=True).click()
            expect(hazard.get_by_role('heading',name='Synthetic test location · open')).to_be_visible()
            capture(hazard,'hazard-existing-metadata.png','Existing shared report display contains neighborhood/category/status/timestamp; filter controls and summary analysis are not implemented.')
            record('Shared hazard display','Authorized synthetic report with metadata','Report displayed; no filters or summary claimed')
            checkin=area('Resident well-being check-in')
            checkin.get_by_label('My status').select_option('safe')
            checkin.get_by_label('Details for your coordinator').fill('Synthetic status, not an actual resident check-in')
            checkin.get_by_role('button',name='Update my status',exact=True).click()
            expect(checkin.get_by_role('heading',name='Synthetic retained draft: Safe')).to_be_visible()
            other_context,other=account('other')
            other.goto('http://127.0.0.1:4500/pages/checklist.html',wait_until='domcontentloaded')
            other_checkin=other.locator('.community-tools section').filter(has=other.get_by_role('heading',name='Resident well-being check-in',exact=True)).last
            expect(other_checkin).to_contain_text('No check-ins to display.')
            assert other_context.request.get(f'http://127.0.0.1:{backend.server_port}/api/check-ins',headers={'Authorization':'Bearer '+accounts['other']['token']}).json()['check_ins']==[]
            capture(other_checkin,'checkin-other-resident-restricted.png','Existing authorization: another synthetic resident sees no check-ins; direct API returns an empty scoped list.')
            guest_context,guest=account()
            guest.goto('http://127.0.0.1:4500/pages/checklist.html',wait_until='domcontentloaded')
            guest_checkin=guest.locator('.community-tools section').filter(has=guest.get_by_role('heading',name='Resident well-being check-in',exact=True)).last
            expect(guest_checkin).to_contain_text('Sign in')
            assert guest_context.request.get(f'http://127.0.0.1:{backend.server_port}/api/check-ins').status==401
            capture(guest_checkin,'checkin-login-required.png','Guest UI requires sign-in; separate direct unauthenticated API request returned 401.')
            record('Shared check-in restriction smoke','Other resident sees none; guest API 401','Both verified; full role matrix still assigned to Ainsley')
            browser.close()
        (EVIDENCE/'browser-cases.json').write_text(json.dumps(cases,indent=2)+'\n')
        (EVIDENCE/'screenshots.json').write_text(json.dumps(images,indent=2)+'\n')
        print(f'{len(cases)} browser scenarios passed, 0 failed; {len(images)} authentic screenshots',flush=True)
    finally:
        backend.shutdown();thread.join();backend.server_close()
