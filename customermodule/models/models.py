# -*- coding: utf-8 -*-

from odoo import models, fields, api

class customermodule(models.Model):
    _name = 'customermodule.customer'

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last name')
    address = fields.Char(string='Address')
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state = fields.Char()
    mobile = fields.Integer(string='Contact')
    email = fields.Char(string='Email')
    pan = fields.Integer(string='Pan')
    aadhar = fields.Integer(string='Aadhar')
    