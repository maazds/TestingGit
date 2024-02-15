# -*- coding: utf-8 -*-
# from odoo import http


# class WorkflowEvaluation(http.Controller):
#     @http.route('/workflow_evaluation/workflow_evaluation', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/workflow_evaluation/workflow_evaluation/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('workflow_evaluation.listing', {
#             'root': '/workflow_evaluation/workflow_evaluation',
#             'objects': http.request.env['workflow_evaluation.workflow_evaluation'].search([]),
#         })

#     @http.route('/workflow_evaluation/workflow_evaluation/objects/<model("workflow_evaluation.workflow_evaluation"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('workflow_evaluation.object', {
#             'object': obj
#         })
