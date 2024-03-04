# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import fields, models

class TestModel(models.Model):
    _name = "test_model"
    _description = "Modelo de prueba"

    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripcion")

class TestModel2(models.Model):
    _name = "test_model2"
    _description = "Modelo de prueba v2"

    names = fields.Char(string="Nombre")
    descriptions = fields.Text(string="Descripcion")

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'
#     _description = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
