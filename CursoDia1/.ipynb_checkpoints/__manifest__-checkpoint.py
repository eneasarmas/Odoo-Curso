# -*- coding: utf-8 -*-
{
    'name' : 'odoo dia 1',
    'summary' : """Dia uno entrenamiento 1255""",
    'description' :"""
        Curso Dia 1 de inicio modificado 1255
    """,
    'author' : 'Crucialsoft',
    'category' : 'Training',
    'version' : '0.0.1',
    'depends' : ['base'],
    'data' : [
        'security/academia_seguridad.xml',
        'security/ir.model.access.csv',
        'views/curso_vista.xml',
        'views/academia_menu.xml',
    ],
    'demo' : [
        'demo/dato_ini.xml',
    ],
}