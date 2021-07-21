# -*- coding: utf-8 -*-

from odoo import models,fields,api

class ProductTemplate(models.Model):
    _inherit='product.template'
    
    is_session_product = fields.Boolean(string='Usar como sesion de producto'
                                        help='Usa esta caja como sesion de seleccion de productos'
                                        default=False)
