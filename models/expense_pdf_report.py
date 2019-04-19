# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ExpensePdfReport(models.TransientModel):
    _inherit = "account.common.account.report"
    _name = "expense.pdf.report"
    _description = "Expense Report"

    employee_ids = fields.Many2many('hr.employee', string='Employees')
    expense_sheet_ids = fields.Many2many(
        string=u'Expenses',
        comodel_name='hr.expense.sheet',
        relation='pdf_report_hr_expense_sheet_rel',
        column1='laporan_id',
        column2='sheet_id',
    )
    
    @api.multi
    def check_report(self):
        self.ensure_one()
        res = super(ExpensePdfReport, self).check_report()

        exp_sheet = self.env['hr.expense.sheet'].search(
            # ['&', '&', ('accounting_date', '>=', self.date_from), ('accounting_date', '<=', self.date_to), ('state', '=', 'paid')])
            [('accounting_date', '>=', self.date_from), ('accounting_date', '<=', self.date_to)])

        if self.employee_ids:
            # data = self.env['hr.expense.sheet'].search(['&', '&', '&', ('accounting_date', '>=', self.date_from), (
            #     'accounting_date', '<=', self.date_to), ('employee_id', 'in', self.employee_ids.ids), ('state', '=', 'paid')])
            exp_sheet = self.env['hr.expense.sheet'].search(['&', '&', ('accounting_date', '>=', self.date_from), (
                'accounting_date', '<=', self.date_to), ('employee_id', 'in', self.employee_ids.ids)])

        print('Jumlah Data : ')
        print(len(exp_sheet))

        # open form view
        self.expense_sheet_ids = [(6, 0, exp_sheet.ids)]

        print('Jumlah Expense Sheet : ')
        print(len(self.expense_sheet_ids))

        return res

    def _print_report(self, data):
        data = self.pre_print_report(data)
        # data['form'].update(self.read(['initial_balance', 'sortby'])[0])
        # if data['form'].get('initial_balance') and not data['form'].get('date_from'):
        #     raise UserError(_("You must define a Start Date"))
        records = self.env[data['model']].browse(data.get('ids', []))
        return self.env['report'].with_context(landscape=True).get_action(records, 'expense_report_mod.laporan_expense_document', data=data)
