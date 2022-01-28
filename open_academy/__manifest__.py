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
        'security/ir.model.access.csv',
        'views/session_views.xml',
        'views/course_views.xml',
    ],
    'demo' : [],
    'auto_install' : False,
    'application' : True,
}
