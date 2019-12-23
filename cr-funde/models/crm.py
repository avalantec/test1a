# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from lxml.etree import tostring, XML

from odoo import api, fields, models
from odoo.osv.orm import setup_modifiers


class Lead(models.Model):
    _inherit = "crm.lead"

    product_id = fields.Many2one("product.product", string="Product")
    quantity_persons = fields.Integer(string="Quantity Persons")

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False,
                        submenu=False):
        res = super(Lead, self).fields_view_get(view_id, view_type, toolbar,
                                                submenu)

        if view_type == 'form':
            doc = XML(res['arch'])
            FIELDS = ['source_id', 'campaign_id', 'medium_id']
            if not self.user_has_groups('sales_team.group_sale_manager'):
                for field in FIELDS:
                    LABEL_STR = "//field[@name='{0}']".format(field)
                    node = doc.xpath(LABEL_STR)
                    if node:
                        node = node[0]
                        node.set("options",
                                 "{'no_create': True, 'no_create_edit': True}")

                    if field in res['fields']:
                        setup_modifiers(node, res['fields'][field])

            res['arch'] = tostring(doc, encoding='unicode')

        return res


class Area(models.Model):
    _name = "partner.area"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")


class Partner(models.Model):
    _inherit = "res.partner"

    quantity_persons = fields.Integer(string="Quantity Persons")
    area_id = fields.Many2one("partner.area", string="Area")

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False,
                        submenu=False):
        res = super(Partner, self).fields_view_get(view_id, view_type, toolbar,
                                                   submenu)

        if view_type == 'form':
            doc = XML(res['arch'])
            if not self.user_has_groups('sales_team.group_sale_manager'):
                node = doc.xpath("//field[@name='area_id']")
                if node:
                    node = node[0]
                    node.set("options",
                             "{'no_create': True, 'no_create_edit': True}")

                setup_modifiers(node, res['fields']['area_id'])

            res['arch'] = tostring(doc, encoding='unicode')

        return res


class SaleOrder(models.Model):
    _inherit = "sale.order"

    quantity_persons = fields.Integer(
        related="partner_id.quantity_persons", store=True)
