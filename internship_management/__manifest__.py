# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2025 ZestyBeanz Technologies(<http://www.zbeanztech.com>)R
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Internship Management',
    'version': '18.0.0.0',
    'summary': 'Module for managing internship applications, student profiles, and feedback.',
    'description': """
        This module facilitates the management of the entire internship process,
        from student application to feedback collection.
        It includes student profiles, internship application tracking,
        and integrates with Odoo's eLearning and Survey modules.
    """,
    'category': 'Human Resources',
    'author': 'Skanda.C, Jeevan V',
    'website': 'www.zbeanztech.com',
    "license": "LGPL-3",
    'depends': [
        'base',             # Core dependency (always needed)
        'mail',             # For chatter and email notifications
        'web',              # Required for reports and UI
        'survey',           # For feedback surveys
        'website_slides',   # For linking internships to eLearning content
        'report_xlsx',      # For Excel reports (optional)
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/report_application.xml',
        'report/report_templates.xml',
        # 'report/application_certificate.xml', # Added for future certificate report
        'views/student_views.xml',
        'views/application_views.xml',
        'views/menu.xml',
        'data/email_templates.xml', # Corrected path to lowercase 'data'
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True, # Changed to True as this is a main application
}