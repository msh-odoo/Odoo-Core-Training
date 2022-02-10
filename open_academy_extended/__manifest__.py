{
    'name' : 'Open Academy Extended',
    'version' : '1.0',
    'category' : 'Tools',
    'summary' : "Updates existing process of managing Course, Session and Attendees",
    'description' : """Improves process of Managing Courses, Session and Attendees
for institutes""",
    'depends' : ['open_academy'],
    'website' : 'http://www.odoo.com',
    'data' : [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/special_course_views.xml',
        'views/res_users_views.xml',
    ],
    'demo' : [],
    'auto_install' : False,
    'application' : False,
}
