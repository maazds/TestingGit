# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WorkflowEval(models.Model):
    _inherit = 'project.task'
    _description = 'Project Task '

    project_task_id = fields.Many2one('project.task', 'Next Task')
    project_task_milestone_ext = fields.Selection([('new', 'New'), ('progress', 'Progress'), ('done', 'Done')],
                                                  'Milestone', default='new')
    workflow_id = fields.Many2one('project.workflow', string="Workflow",required=True)
    workflow_id_ext = fields.Many2one('workflow.in', string="Select Workflow",required=True)

