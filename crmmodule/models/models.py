# -*- coding: utf-8 -*-

from odoo import models, fields, api

SOURCE = [
    ('Email','Email'),
    ('Telephone','Telephone'),
    ('Website','Website'),
]

class crmmodule(models.Model):
    _inherit = 'crm.lead'
    
    source = fields.Selection(SOURCE ,string='Source', required='True')
    email = fields.Char(string='Email')
    telephone = fields.Char(string='Telephone')
    website = fields.Char(string='Website')
    address = fields.Many2one('res.partner',string="Address")
