from odoo import models, fields, api

class ticket_system_teams(models.Model):
    _name = 'ticket_system.teams'
    
    name = fields.Char()
    description = fields.Text()
    member_ids = fields.Many2many('res.users',string="Team Members")
    assignment_method = fields.Selection([('Balanced','Balanced'),('Manual','Manual'),('Random','Random')],string="Assignment Method",default='Manual')
    use_alias = fields.Boolean(string="Email Alias",default=True)
