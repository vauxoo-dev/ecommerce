# coding: utf-8
# Copyright 2016 Vauxoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import http
from openerp.http import request


class WebsiteHr(http.Controller):
    @http.route(['/demo_hr'], type='http', auth='public', website=True)
    def get_hr(self, **post):
        employees_obj = request.env['hr.employee']._get_employees()
        values = {
            'employees': employees_obj,
        }
        return request.website.render('controller_demo.demo_hr_template', values)
