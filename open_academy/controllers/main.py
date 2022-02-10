from odoo import http
from odoo.http import request

class OpenAcademy(http.Controller):

    @http.route('/hello', auth="public")
    def hello(self, **kw):
        return "Hello World!"

    @http.route('/hello_user', auth="user")
    def hello_usr(self, **kw):
        return "Hello %s" %(request.env.user.name)

    