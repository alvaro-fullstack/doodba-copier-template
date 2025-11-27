from odoo import fields, models

class VisiotechTest(models.Model):
    _name = 'vt.test'
    _description = 'Modelo de Prueba Visiotech'

    name = fields.Char(string='Nombre de Prueba', required=True)
