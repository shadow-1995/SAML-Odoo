# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ticket_system(models.Model):
    _name = 'ticket_system.ticket_system'

    name = fields.Char()
    helpdesk_team = fields.Char(string="Team")
    assigned_to = fields.Char(string="Assigned To")
    active_button = fields.Boolean(default=True)
    priority = fields.Selection([('Low','Low'),('Medium','Medium'),('High','High')],string="Priority")
    customer_id = fields.Many2one('res.partner',String="Customer")
    customer_name = fields.Char(string="Customer Name")
    customer_email = fields.Char(string="Customer E-mail")
    ticket_type = fields.Char(string="Ticket Type")
    ticket_tag = fields.Char(string="Ticket Tag")
    
    
    def assign_ticket_to_self(self):
        pass
