from odoo import http
from odoo.http import request

class OpenAcademy(http.Controller):

    @http.route('/hello', auth="public")
    def hello(self, **kw):
        return "Hello World"

    @http.route('/hello_user', auth="user")
    def hello_user(self, **kw):
        return "Hello %s" %(request.env.user.name)

    @http.route('/hello_template')
    def hello_template(self, **kw):
        return request.render('open_academy.hello_world')

    @http.route('/hello_template_user')
    def hello_template_user(self, **kw):
        courses = request.env['course.course'].search([('state', '=', 'confirm')])
        print ("courses ::: ", courses)
        return request.render('open_academy.hello_user', { 'user': request.env.user, 'courses': courses })

    @http.route(['/course', '/course/static/<string:is_static>'], auth="public", website=True)
    def courses(self, is_static=False, **kw):
        if is_static:
            return request.render('open_academy.courses_static', {
                'courses': request.env['course.course'].sudo().search([], limit=8)
            })
        return request.render('open_academy.courses', {
                'courses': request.env['course.course'].sudo().search([], limit=8)
            })

    @http.route(['/course/<model("course.course"):course>', '/course/<string:is_static>'], auth="public", website=True)
    def course_details(self, course=False, **kw):
        if course:
            return request.render('open_academy.course_details', {
                'course': course,
            })
        