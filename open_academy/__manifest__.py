{
    'name' : 'Open Academy',
    'version' : '1.0',
    'category' : 'Tools',
    'summary' : " Courses, Sessions, Attendees",
    'description' : """Manages Courses, Session and Attendees
for institutes""",
    'depends' : ['mail'],
    'website' : 'http://www.odoo.com',
    'data' : [
        'security/open_academy_security.xml',
        'security/ir.model.access.csv',
        'views/open_academy_menus.xml',
        'views/session_views.xml',
        'views/course_views.xml',
        'wizard/assign_instructor_views.xml',
        'views/open_academy_templates.xml',
    ],
    'demo' : [],
    'auto_install' : False,
    'application' : True,
}
