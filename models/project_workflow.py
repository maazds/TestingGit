from odoo import api, models, fields


class ProjectWorkflow(models.Model):
    _name = 'project.workflow'
    _description = 'Defining a workflow'

    name = fields.Char(string='Workflow Name')
    Workflow_name = fields.Many2one('workflow.in', 'Workflow', store=True)
    description = fields.Text(string='Description')
    project_id = fields.Many2one('project.project', string='Project',store=True)
    task_temp_ongoing = fields.One2many('project.task', 'workflow_id', string='Ongoing Tasks',store=True)
    task_temp_next = fields.One2many('project.task', 'workflow_id', string='Next Tasks',store=True)
    task_temp_upnext = fields.One2many('project.task', 'workflow_id', string='Up Next',store=True)

    @api.onchange('Workflow_name')
    def change_description(self):
        if self.Workflow_name:
            workflow = self.env['workflow.in'].browse(self.Workflow_name.ids)
            # print(workflow)
            self.write({'description': workflow.description})

    @api.onchange('Workflow_name')
    def change_ongoing(self):
        for rec in self:
            if rec.Workflow_name:
                workflow = self.env['project.task'].search([('workflow_id_ext', '=', rec.Workflow_name.id)]).ids
                for i in workflow:
                    rec.task_temp_ongoing = [(6, 0, workflow[:1])]

    @api.onchange('Workflow_name')
    def change_next(self):
        for rec in self:
            if rec.Workflow_name:
                workflow = self.env['project.task'].search([('workflow_id_ext', '=', rec.Workflow_name.id)]).ids
                if workflow:
                    for i in workflow:
                        rec.task_temp_next = [(6, 0, workflow[1:2])]

    @api.onchange('Workflow_name')
    def change_upnext(self):
        for rec in self:
            if rec.Workflow_name:
                workflow = self.env['project.task'].search([('workflow_id_ext', '=', rec.Workflow_name.id)]).ids
                if workflow:
                    for i in workflow:
                        rec.task_temp_upnext = [(6, 0, workflow[2:])]
