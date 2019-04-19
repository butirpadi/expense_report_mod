# -*- coding: utf-8 -*-
{
    'name': "Expense PDF Report",

    'summary': """
        Expense PDF Report""",

    'description': """
        Expense PDF Report
    """,

    'author': "Tepat Guna Karya",
    'website': "http://www.tepatguna.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Employees',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'hr_expense'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/expense_report.xml',
        'views/wizard_expense_report.xml',
        'views/expense_detail.xml',
        # 'views/expense_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}