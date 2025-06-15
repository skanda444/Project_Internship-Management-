from odoo import models, fields

class InternshipStudent(models.Model):
    _name = 'internship.student'
    _description = 'Student Profile'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    roll_no = fields.Char(string='Roll Number', required=True)
    department = fields.Char(string='Department')
    course = fields.Char(string='Course')
    cgpa = fields.Float(string='CGPA')
    resume = fields.Binary(string='Resume')
    resume_filename = fields.Char(string='Resume Filename')
