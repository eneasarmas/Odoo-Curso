# -*- coding: utf-8 -*-
{
    'name' : 'odoo Academy',
    'summary' : """Academy app training""",
    'description' :"""
        Academy curses
    """,
    'author' : 'crucialsoft',
    'category' : 'Training',
    'version' : '0.0.1',
    'depends' : ['sale','web_cohort','website'],
    'data' : [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/css_loader.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_templates.xml',
        'views/academy_web_templates.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
}