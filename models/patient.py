from odoo import api, fields, models


class Hospitalpatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital patient model"

    patientName = fields.Char(string="Name")
    patientAge = fields.Integer(string="Age")
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
    ], string="Gender")

