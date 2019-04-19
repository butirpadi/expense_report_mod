# -*- coding: utf-8 -*-
from odoo import http

# class ExpenseReportMod(http.Controller):
#     @http.route('/expense_report_mod/expense_report_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/expense_report_mod/expense_report_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('expense_report_mod.listing', {
#             'root': '/expense_report_mod/expense_report_mod',
#             'objects': http.request.env['expense_report_mod.expense_report_mod'].search([]),
#         })

#     @http.route('/expense_report_mod/expense_report_mod/objects/<model("expense_report_mod.expense_report_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('expense_report_mod.object', {
#             'object': obj
#         })