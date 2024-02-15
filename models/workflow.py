from odoo import api,fields,models

class Workflowin(models.Model):
    _name = 'workflow.in'
    _description = 'workflow name'

    name = fields.Char(string='Workflow Name')
    description = fields.Text(string='Description')