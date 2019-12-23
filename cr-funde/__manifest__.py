# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Customize CRM",
    "version": "11.0.0.1",
    "license": "LGPL-3",
    "author": "Odoo S.A.",
    "website": "www.odoo.com",
    "category": "CRM",
    "depends": ['crm', 'product', 'sale'],
    "data": [
        "security/ir.model.access.csv",
        "views/area_views.xml",
        "views/crm_views.xml",
        "views/partner_views.xml",
        "views/sales-report-template.xml",
        "views/crm_source_views.xml",
    ],
    "installable": True,
}
