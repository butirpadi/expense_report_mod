# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class LaporanExpense(models.TransientModel):
    _name = "laporan.expense"
    _description = "Expense Report"

    date_from = fields.Date('Start Date', required=True)
    date_to = fields.Date('Start Date', required=True)
    employee_ids = fields.Many2many('hr.employee', string='Employees')
    employee_id = fields.Many2one('hr.employee', string='Employees')
    expense_sheet_ids = fields.Many2many(
        string=u'Expenses',
        comodel_name='hr.expense.sheet',
        relation='laporan_hr_expense_sheet_rel',
        column1='laporan_id',
        column2='sheet_id',
    )    
    report_type = fields.Selection(
        string=u'Report Type',
        selection=[('sum', 'Summary'), ('detail', 'Detail')],
        default='sum'
    )
    

    @api.multi
    def get_report(self):
        report_obj = self.env['report']
        template = 'expense_report_mod.travel_expense_report_document'
        report = report_obj._get_report_from_name(template)

        domain = {
            'date_from': self.date_from,
            'date_to': self.date_to,
            'employee_id': self.employee_id.id,
            'report_type': self.report_type,
        }

        vals = {
            'ids': self.ids,
            'model': report.model,
            'form': domain
        }

        """get_action() otomatis akan memanggil render_html() di report"""
        return report_obj.get_action(self, template, data=vals)

    # @api.multi
    # def check_report(self):
    #     self.ensure_one()
    #     print('test inside report expense')
    #     data = self.env['hr.expense.sheet'].search(
    #         # ['&', '&', ('accounting_date', '>=', self.date_from), ('accounting_date', '<=', self.date_to), ('state', '=', 'paid')])
    #         [('accounting_date', '>=', self.date_from), ('accounting_date', '<=', self.date_to)])

    #     if self.employee_ids:
    #         # data = self.env['hr.expense.sheet'].search(['&', '&', '&', ('accounting_date', '>=', self.date_from), (
    #         #     'accounting_date', '<=', self.date_to), ('employee_id', 'in', self.employee_ids.ids), ('state', '=', 'paid')])
    #         data = self.env['hr.expense.sheet'].search(['&', '&', ('accounting_date', '>=', self.date_from), (
    #             'accounting_date', '<=', self.date_to), ('employee_id', 'in', self.employee_ids.ids)])

    #     print('Jumlah Data : ')
    #     print(len(data))

    #     # open form view
    #     self.expense_sheet_ids = [(6, 0, data.ids)]

    #     print('Jumlah Expense Sheet : ')
    #     print(len(self.expense_sheet_ids))

    #     # open report
    #     # return self.env.ref('expense_report_mod.laporan_expense_document').report_action(self)
    #     # return {'type': 'ir.actions.report','report_name': 'expense_report_mod.action_laporan_expense_document','report_type':"qweb-pdf"}
    #     # self._context.update( { 'key': 'val' } )

    #     return {
    #         'type': 'ir.actions.report.xml',
    #         'report_name': 'expense_report_mod.travel_expense_report_document',
    #         'context':self._context,
    #     }

    # @api.multi
    # def check_report(self):
    #     self.ensure_one()
    #     print('Inside Check Report Expense')
    #     # data = {}
    #     # data['ids'] = self.env.context.get('active_ids', [])
    #     # data['model'] = self.env.context.get('active_model', 'ir.ui.menu')
    #     # data['form'] = self.read(['date_from', 'date_to', 'journal_ids', 'target_move'])[0]
    #     # used_context = self._build_contexts(data)
    #     # data['form']['used_context'] = dict(used_context, lang=self.env.context.get('lang') or 'en_US')
    #     # return self._print_report(data)
