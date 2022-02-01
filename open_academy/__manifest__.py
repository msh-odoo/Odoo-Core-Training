# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Open Academy',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'Manages Course, Sessions and Attendees',
    'description': """
This module manages Courses and it's Sessions and attendees
who attends those sessions.""",
    'website': 'https://www.odoo.com/app/crm',
    'depends': [
        'mail',
    ],
    'data': [
        'security/open_academy_security.xml',
        'security/ir.model.access.csv',
        'data/open_academy_data.xml',
        'wizard/session_wizard_views.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/open_academy_templates.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
