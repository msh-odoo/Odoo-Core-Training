# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Open Academy Extended',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'Improves Course, Sessions and Attendees Process',
    'description': """
This module extends Open Academy and improves few process""",
    'website': 'https://www.odoo.com/app/crm',
    'depends': [
        'mail',
        'open_academy'
    ],
    'data': [
        # 'security/crm_security.xml',
        # 'security/ir.model.access.csv',
        # 'views/course_views.xml',
        # 'views/session_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
