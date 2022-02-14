from odoo import http
from odoo.http import request

class OpenAcademy(http.Controller):

    @http.route('/hello', auth="public")
    def hello(self, **kw):
        return "Hello World!"

    @http.route('/hello_user', auth="user")
    def hello_usr(self, **kw):
        return "Hello %s" %(request.env.user.name)

    @http.route('/my_template', auth="public")
    def my_template(self, **kW):
        return request.render("open_academy.my_template", {})

    @http.route('/my_template_user', auth="user")
    def my_template_user(self, **kw):
        return request.render("open_academy.my_template_user", {
            'name': request.env.user.name
        })

    @http.route('/qweb_directives', auth="user")
    def qweb_directives(self, **kw):
        courses = request.env['course.course'].search([])
        return request.render("open_academy.qweb_template_example", {
            'courses': courses,
            'colors': {
                0: 'green',
                1: '#000000',
                2: 'red',
                3: 'grey',
            }
        })

    @http.route('/test_tcall', auth="user")
    def test_call(self, **kw):
        return request.render('open_academy.test_tcall', {})

    @http.route('/web_page', auth="user", website=True)
    def web_page(self, **kw):
        courses = request.env['course.course'].search([])
        return request.render("open_academy.web_page", {
            'courses': courses,
            'colors': {
                0: 'green',
                1: '#000000',
                2: 'red',
                3: 'grey',
            }
        })

    @http.route('/course_details/<model("course.course"):course>', auth="user", website=True)
    def course_details(self, course=None, **kw):
        return request.render("open_academy.course_details", {
            'course': course,
        })
