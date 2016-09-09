# coding: utf-8
# Copyright 2016 Vauxoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, api


class Hr(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def _get_employees(self):
        employees_obj = self.sudo().search([])
        return employees_obj
