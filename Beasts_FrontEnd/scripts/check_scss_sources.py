#!/usr/bin/env python3
"""Check migrated SCSS source ownership and browser URLs after make preview-build."""
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REPORT = Path(__file__).with_name('scss-migration.json')


def main():
    report = json.loads(REPORT.read_text())
    for row in report['standalone']:
        assert not (ROOT / row['old']).exists(), f"Duplicate CSS source: {row['old']}"
        assert (ROOT / row['entry']).read_text().startswith('---\n---\n'), row['entry']
        assert (ROOT / row['partial']).is_file(), row['partial']
        compiled = ROOT / '_site' / row['old']
        assert compiled.is_file(), f"Missing browser stylesheet: {compiled}"
        assert '$beasts-' not in compiled.read_text(), f"Uncompiled Sass: {compiled}"
    for row in report['inline']:
        assert (ROOT / row['partial']).is_file(), row['partial']
        import_name = row['partial'].removeprefix('_sass/').removesuffix('.scss').replace('/_', '/')
        assert import_name in (ROOT / row['file']).read_text(), row['file']
    for row in report['static_html']:
        assert (ROOT / row['entry']).read_text().startswith('---\n---\n'), row['entry']
        assert (ROOT / row['partial']).is_file(), row['partial']
        assert (ROOT / '_site' / row['url']).is_file(), row['url']
        relative_url = os.path.relpath(row['url'], Path(row['file']).parent)
        assert f'href="{relative_url}"' in (ROOT / row['file']).read_text(), row['file']
    for path in (ROOT / '_sass' / 'beasts').rglob('*.scss'):
        for name in re.findall(r'@import "(beasts/[^"]+)";', path.read_text()):
            target = ROOT / '_sass' / name
            assert target.with_name('_' + target.name).with_suffix('.scss').is_file(), name
    print(f"PASS: {len(report['standalone'])} compiled CSS URLs, "
          f"{len(report['inline'])} inline SCSS imports, "
          f"{len(report['static_html'])} static-page stylesheets, no duplicate CSS sources.")


if __name__ == '__main__':
    main()
