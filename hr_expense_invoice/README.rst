================================
Supplier invoices on HR expenses
================================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:af2edde4920f205fd7b250d53967f0f5ad5e188f38bf974e8ee1b8a4c184fb06
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fhr-lightgray.png?logo=github
    :target: https://github.com/OCA/hr/tree/12.0/hr_expense_invoice
    :alt: OCA/hr
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/hr-12-0/hr-12-0-hr_expense_invoice
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/hr&target_branch=12.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module should be used when a supplier invoice is paid by an employee. It
allows to set a supplier invoice for each expense line, adding the
corresponding journal items to transfer the debt to the employee.

There are 2 ways to reference expense to invoice.

1. On expense, directly select one invoice.
2. On expense report, use button "Create Vendor Bill" to create one invoice
   for multiple expenses.

**Table of contents**

.. contents::
   :local:

Usage
=====

**Reference one invoice to an expense**

* Create an expense sheet.
* Add an expense line to sheet with an invoice_id selected or create one new.
* Process expense sheet.
* On paying expense sheet, you are reconciling supplier invoice too.

**Create one invoice to multiple expenses**

* Create an expense sheet with one or multiple expense lines
* After approved, click button "Create Vendor Bill"
* Select multiple expense to create an invoice, and process it.
* New invoice will be create and link to the selected expense lines.
* Validate newly create invoice.
* On paying expense sheet, you are reconciling supplier invoice(s) too.

Known issues / Roadmap
======================

* Multiple payment terms for a supplier invoice are not handled correctly.
* Partial reconcile supplier invoices are also not correctly handled.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/hr/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/hr/issues/new?body=module:%20hr_expense_invoice%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* Tecnativa

Contributors
~~~~~~~~~~~~

* `Tecnativa <https://www.tecnativa.com>`_:

  * Pedro M. Baeza
  * Vicent Cubells
  * Víctor Martínez

* Kitti Upariphutthiphong <kittiu@ecosoft.co.th>

Maintainers
~~~~~~~~~~~

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/hr <https://github.com/OCA/hr/tree/12.0/hr_expense_invoice>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
