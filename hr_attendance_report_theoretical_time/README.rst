=====================================
Theoretical vs Attended Time Analysis
=====================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:98e8a7441463d7c9c7326a3def3d3c0d56eaac5d658bee40da50b15ecd259eef
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fhr-lightgray.png?logo=github
    :target: https://github.com/OCA/hr/tree/12.0/hr_attendance_report_theoretical_time
    :alt: OCA/hr
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/hr-12-0/hr-12-0-hr_attendance_report_theoretical_time
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/hr&target_branch=12.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module adds a new report called "Theoretical vs Attended Time Analysis"
that compares worked time, measured through attendances records, with the
theoretical time, computed from employee's working calendar, public holidays
and employee specific leaves. Missing attendance days are generated on the fly
in the report with their corresponding theoretical hours.

There is the possibility of counting as theoretical time some leave types if
specified in them.

As an example, imagine a work week with 40 theoretical hours, and these
attendance situation:

* Monday: Worked 10 hours
* Tuesday: Worked 10 hours
* Wednesday: Worked 10 hours
* Thursday: Worked 10 hours
* Friday: Ask for a compensation leave (said leave type), as already worked
  40 hours.

On the report, whole week should put 40 theoretical hours - 8 per day - against
40 worked hours (although they were on previous days, and none on Friday).

On contrary, if you want to take a holiday one of that days, you should ask for
a leave type without the check for counting as theoretical time, and then the
whole week will be 32 theoretical hours against the worked hours of that week
without the leave.

**Table of contents**

.. contents::
   :local:

Installation
============

On installation time, this module computes the theoretical hours for the day of
the attendance check-in, so if you have a lot of records, this would be a bit
slow.

Configuration
=============

You need to be at least "Attendance / Manual Attendance" for being able to see
the attendances report.

For including some leave types in the theoretical time, you have to:

#. Go to *Leaves > Configuration > Leave Types*.
#. Select leave type you want to include.
#. Check the mark "Include in theoretical hours".

When generating non worked days, this module uses a start date for beginning
the series generation, which is:

* Manual start date set on the employee.
* If not set, the greatest of these 2 dates:

  * Employee creation date.
  * Working calendar line start date.

For configuring manual start date, you have to:

#. Go to *Employees > Employees*.
#. Select an employee.
#. Go to "HR Settings" page.
#. Set the date in "Theoretical hours start date" field.

The generation will stop on the end date of the working calendar line or today,
so don't forget to properly set start and end dates of the lines of the working
calendar for not leaving empty spaces between them.

Usage
=====

#. Go to *Attendances > Reporting > Theoretical vs Attended Time Analysis*.
#. Check pivot table or look at the graph view.

Known issues / Roadmap
======================

* Employees with less than 1 week in the company will show full week
  theoretical hours.
* Activate ORM cache for improving performance on computing theoretical hours,
  but assuring that the cache is cleared when the conditions of the computation
  changes.
* If you change employee's working time, theoretical hours for non attended
  days will be computed according this new calendar. You have to define
  start and end dates inside the calendar for avoiding this side effect.
* Theoretical hours of affected days when changing the leave type to be
  included or not in theoretical time are not recomputed.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/hr/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/hr/issues/new?body=module:%20hr_attendance_report_theoretical_time%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com>`__:

  * Pedro M. Baeza.
  * David Vidal
  * Víctor Martínez

Other credits
~~~~~~~~~~~~~

**Images**

* Font Awesome: `Icon <http://fontawesome.io>`_.

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/hr <https://github.com/OCA/hr/tree/12.0/hr_attendance_report_theoretical_time>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
