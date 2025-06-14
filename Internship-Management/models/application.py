from odoo import models, fields, api

class InternshipApplication(models.Model):
    _name = 'internship.application'
    _description = 'Internship Application'

    student_id = fields.Many2one('internship.student', string='Student', required=True)
    internship_id = fields.Many2one('slide.channel', string='Internship', required=True, domain="[('channel_type', '=', 'training')]")
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed')
    ], default='draft', string='Status')

    applied_date = fields.Date(string='Applied On', default=fields.Date.today)

    @api.model
    def create(self, vals):
        vals['status'] = 'submitted'
        return super(InternshipApplication, self).create(vals)
