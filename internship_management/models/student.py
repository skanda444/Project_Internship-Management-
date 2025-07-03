from odoo import models, fields, api
from odoo.exceptions import ValidationError

class InternshipStudent(models.Model):
    _name = 'internship.student'
    _description = 'Student Profile'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    roll_no = fields.Char(string='Roll Number', required=True, copy=False) # Added copy=False for unique identifiers
    department = fields.Char(string='Department')
    cgpa = fields.Float(string='CGPA')
    resume = fields.Binary(string='Resume File', required=True, attachment=True, filters='*.pdf') # Only accept PDF files
    resume_filename = fields.Char(string='Resume Filename')

    # One2many field to link to internship applications
    application_ids = fields.One2many(
        'internship.application',
        'student_id',
        string='Internship Applications'
    )

    # SQL Constraint for uniqueness of Roll Number and Email
    _sql_constraints = [
        ('roll_no_unique', 'unique(roll_no)', 'The Roll Number must be unique!'),
        ('email_unique', 'unique(email)', 'The Email must be unique!'),
    ]

    # Removed print_application_report and send_application_report_email as they belong to application model
    # If you need student-specific reports, add new methods and XML definitions for them.

    @api.constrains('resume', 'resume_filename')
    def _check_resume_pdf(self):
        for rec in self:
            if rec.resume and rec.resume_filename:
                if not rec.resume_filename.lower().endswith('.pdf'):
                    raise ValidationError('Resume file must be a PDF.')