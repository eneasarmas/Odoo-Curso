# -*- coding: utf-8 -*-

from odoo import models,fields,api

class SaleWizard(models.Model):
    _name = 'academy.sale.wizard'
    _description = 'Asistente: Ordenes de venta rapidas para sesiones de estudiantes'
    
    def _default_session(self):
        return self.env['academy.session'].browser(self._context.get('active_id'))

    session_id = fields.Many2one(comodel_name='academy.session'
                              ,string='Sesion'
                              ,required=True
                              ,default=_default_session
                 )

    session_student_ids = fields.Many2many(comodel_name='res.partner'
                              ,string='Estudiante en la sesion actual'
                              ,related='session_id.students_ids'
                              ,help='Estos son los estudiantes en la sesion actual'
                          )

    students_ids = fields.Many2many(comodel_name='res.partner'
                            ,string='Estudiantes para orden de venta'
                   )
    
    def create_ale_orders(self):
        session_product_id = self.env['product.product'].search([('is_session_product','=',True)],limit=1)
        if session_product_id:
            for student in self.students_ids:
                order_id = self.env['sale.order'].create({
                    'partner': student.id
                    ,'session_id':self.session_id.id
                    ,'order_line': [(0,0,{'product_id':session_product_id.id,'price_unit':self.session_id.total_price})]
                })
    
