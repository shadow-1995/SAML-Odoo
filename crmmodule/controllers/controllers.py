# -*- coding: utf-8 -*-
from odoo import http

# class Crmmodule(http.Controller):
#     @http.route('/crmmodule/crmmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crmmodule/crmmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crmmodule.listing', {
#             'root': '/crmmodule/crmmodule',
#             'objects': http.request.env['crmmodule.crmmodule'].search([]),
#         })

#     @http.route('/crmmodule/crmmodule/objects/<model("crmmodule.crmmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crmmodule.object', {
#             'object': obj
#         })