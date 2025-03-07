# Copyright (C) 2018 Brainbean Apps (https://brainbeanapps.com)
# Copyright 2020 CorporateHub (https://corporatehub.eu)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    'name': 'Leave Credit',
    'version': '12.0.1.1.0',
    'category': 'Human Resources',
    'website': 'https://github.com/OCA/hr',
    'author':
        'CorporateHub, '
        'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'summary': 'Enable negative leave balance for employees',
    'depends': [
        'hr_holidays',
    ],
    'data': [
        'views/hr_leave_type.xml',
    ],
}
