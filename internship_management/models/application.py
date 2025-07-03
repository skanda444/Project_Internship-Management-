from odoo import models, fields, api
from odoo.exceptions import UserError

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
    ], default='draft', string='Status', store=True)

    applied_date = fields.Date(string='Applied On', default=fields.Date.today, readonly=True)
    start_date = fields.Date(string='Internship Start Date')
    end_date = fields.Date(string='Internship End Date')

    approval_state = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Approval Status', default='pending')

    def print_application_report(self):
        try:
            return self.env.ref('internship_management.action_report_internship_application').report_action(self)
        except ValueError:
            raise UserError("Report template not found. Please contact administrator to configure reports.")

    def send_application_report_email(self):
        try:
            self.ensure_one() # Ensure method is called on a single record
            template = self.env.ref('internship_management.email_template_internship_application_report')
            template.send_mail(self.id, force_send=True)
        except ValueError:
            raise UserError("Email template not found. Please contact administrator to configure email templates.")

    # Optional: Method to send status update email (can be called by a button or automated action)
    def action_send_status_email(self):
        self.ensure_one()
        template = self.env.ref('internship_management.email_application_status_template')
        template.send_mail(self.id, force_send=True)

    # Method to generate summary report
    def print_summary_report(self):
        return self.env.ref('internship_management.action_report_internship_summary').report_action(self)

    def print_certificate(self):
        if self.status != 'completed':
            raise UserError('You can only print the certificate when the status is Completed.')
        return self.env.ref('internship_management.action_report_internship_certificate').report_action(self)

    def create(self, vals_list):
        # Handle both single dict and list of dicts
        if isinstance(vals_list, dict):
            vals_list = [vals_list]
        for vals in vals_list:
            student = self.env['internship.student'].browse(vals.get('student_id'))
            if student and student.cgpa < 8.0:
                raise UserError('Only students with CGPA 8.0 or above can apply for internship.')
        return super().create(vals_list)

    def write(self, vals):
        if 'student_id' in vals:
            student = self.env['internship.student'].browse(vals['student_id'])
            if student and student.cgpa < 8.0:
                raise UserError('Only students with CGPA 8.0 or above can apply for internship.')
        # If status is being set to 'submitted', also set approval_state to 'pending'
        if 'status' in vals and vals['status'] == 'submitted':
            vals['approval_state'] = 'pending'
        return super().write(vals)

    def action_submit_application(self):
        for rec in self:
            if rec.status != 'draft':
                raise UserError('You can only submit a draft application.')
            rec.status = 'submitted'
            rec.approval_state = 'pending'

    def action_approve_application(self):
        for rec in self:
            if rec.status != 'submitted':
                raise UserError('You can only approve a submitted application.')
            rec.status = 'approved'
            rec.approval_state = 'approved'

    def action_reject_application(self):
        for rec in self:
            if rec.status != 'submitted':
                raise UserError('You can only reject a submitted application.')
            rec.status = 'rejected'
            rec.approval_state = 'rejected'

    def action_toggle_completed(self):
        for rec in self:
            if rec.status != 'approved':
                raise UserError('You can only mark an approved application as completed.')
            rec.status = 'completed'
   