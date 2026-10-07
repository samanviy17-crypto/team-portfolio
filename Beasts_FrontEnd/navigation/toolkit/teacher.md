---
layout: post
title: Teacher Toolkit
description:
permalink: /teacher
menu: nav/homejava.html
show_reading_time: false
---

<div class="container">
    <div class="student-management glowOnHover"
        onclick="location.href='{{site.baseurl}}/teacher-toolkit/period1';" style="cursor: pointer;">
        <div class="student-management-image">
            <img src="{{site.baseurl}}/images/toolkit-nav-buttons/studentmanagement.png" alt="student-management" />
        </div>
        <div class="student-management-details">
            <h3>Student Management</h3>
            <p>This tool lets you:</p>
            <ul>
                <li>Track students at each table per period</li>
                <li>See what each student is doing and monitor assigned tasks</li>
                <li>Track the progress of each student</li>
                <li>View students' GitHub activity</li>
            </ul>
        </div>
    </div>
</div>

<style>
{{ '@import "beasts/inline/navigation/navigation-toolkit-teacher-1";' | scssify }}
</style>
