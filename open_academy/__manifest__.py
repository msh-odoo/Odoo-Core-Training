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
        # 'security/crm_security.xml',
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
