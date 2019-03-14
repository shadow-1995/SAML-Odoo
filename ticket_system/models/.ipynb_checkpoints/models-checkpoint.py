# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ticket_system(models.Model):
    _name = 'ticket_system.ticket_system'

    name = fields.Char()
    helpdesk_team = fields.Char(string="Team")
    assigned_to = fields.Char(string="Assigned To")
    priority = fields.Selection([('Low','Low'),('Medium','Medium'),('High','High')],string="Priority")
    customer_id = fields.Many2one('res.partner',String="Customer")
    customer_name = fields.Char(string="Customer Name")
    stage = fields.Selection([('New','New'),('In Progress','In Progress'),('Solved','Solved'),('Cancelled','Cancelled')],string="Stage")
    customer_email = fields.Char(string="Customer E-mail")
    ticket_type = fields.Char(string="Ticket Type")
    ticket_tag = fields.Char(string="Ticket Tag")
    
