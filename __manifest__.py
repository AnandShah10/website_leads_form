# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'website_leads_form',
    'version': '1.2',
    'summary': "Leads Form",
    'sequence': 17,
    'author': "anand",
    'description': """
Leads Form Pgge module
""",
    'category': 'Custom/Website',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['mail', 'website'],
    'data': [
'views/templates.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
