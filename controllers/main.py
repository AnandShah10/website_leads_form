from odoo import http
from odoo.http import content_disposition, Controller, request, route
from odoo import _
from odoo.exceptions import ValidationError, UserError


class CRMLeads(http.Controller):

    @http.route(['/create_leads_form'], website=True, auth='user')
    def leads_create_form(self, **kw):
        partners = request.env['res.partner'].search([])
        return request.render('website_leads_form.create_leads_form', {'partners': partners})

    @http.route(['/create_leads'], website=True, auth='user')
    def crm_create_create(self, **kw):
        print("yyyyyyyyyyyyyyyyyyyy")
        leads = request.env['crm.lead'].create(kw)
        print("^^^^^^^^^^^", leads)
        return request.render('website_leads_form.leads_submit_success', {})
