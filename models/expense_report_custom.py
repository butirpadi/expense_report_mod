from datetime import datetime
from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT
from pprint import pprint


class ExpenseReportCustom(models.AbstractModel):
    """
    # Report untuk menggenerate custom report
    # _name diisi dengan pola 'report.module_name.report_name'
    # _template diisi dengan pola 'module_name.report_name'
    """

    _name = 'report.expense_report_mod.travel_expense_report_document'
    _template = 'expense_report_mod.travel_expense_report_document'

    @api.model
    def render_html(self, docids, data=None):
        if data is None:
            return

        date_from = data['form']['date_from']
        date_to = data['form']['date_to']
        employee_id = data['form']['employee_id']
        report_type = data['form']['report_type']

        report_obj = self.env['report']
        docs = self._get_rekap_data(date_from, date_to, employee_id, report_type)

        LOCAL_FORMAT = '%d/%m/%Y'

        vals = {
            'docs': docs,
            'date_from': datetime.strptime(date_from, DATE_FORMAT).strftime(LOCAL_FORMAT),
            'date_to': datetime.strptime(date_to, DATE_FORMAT).strftime(LOCAL_FORMAT),
            'employee_id': self.env['hr.employee'].search([('id', '=', employee_id)]),
            'report_type' : report_type
        }

        return report_obj.render(self._template, values=vals)

    def _get_rekap_data(self, date_from, date_to, employee_id, report_type):
        """
        return [
                {
                        'employee': "employee 1 name",
                        'presensi': count_of_presence,
                        'absensi': count_of_absence,
                },
                {
                        'employee': "employee 2 name",
                        'presensi': count_of_presence,
                        'absensi': count_of_absence,
                }
        ]
        """

        date_from_obj = datetime.strptime(date_from, DATE_FORMAT).date()
        date_to_obj = datetime.strptime(date_to, DATE_FORMAT).date()
        date_count = (date_to_obj - date_from_obj).days + 1

        datares = []

        # get all data

        data = self.env['hr.expense.sheet'].search(
            ['&', '&', ('accounting_date', '>=', date_from), ('accounting_date', '<=', date_to), ('state', 'in', ['post','done'])],order="accounting_date asc")
            
        if employee_id:
            data = self.env['hr.expense.sheet'].search(['&', '&', '&', ('accounting_date', '>=', date_from),
                        ('accounting_date', '<=', date_to), ('employee_id', '=', employee_id), ('state', 'in', ['post','done'])])


        return data
