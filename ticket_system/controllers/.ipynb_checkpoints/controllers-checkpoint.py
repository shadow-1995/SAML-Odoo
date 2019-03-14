# -*- coding: utf-8 -*-
from odoo import http

class TicketSystem(http.Controller):
    @http.route('/ticket_system/ticket_system/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/ticket_system/ticket_system/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('ticket_system.listing', {
            'root': '/ticket_system/ticket_system',
            'objects': http.request.env['ticket_system.ticket_system'].search([]),
        })

    @http.route('/ticket_system/ticket_system/objects/<model("ticket_system.ticket_system"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('ticket_system.object', {
            'object': obj
        })