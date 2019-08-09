# -*- coding: utf-8 -*-
from odoo import http

# class Customermodule(http.Controller):
#     @http.route('/customermodule/customermodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customermodule/customermodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customermodule.listing', {
#             'root': '/customermodule/customermodule',
#             'objects': http.request.env['customermodule.customermodule'].search([]),
#         })

#     @http.route('/customermodule/customermodule/objects/<model("customermodule.customermodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customermodule.object', {
#             'object': obj
#         })