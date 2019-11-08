# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "EDI - Proforma Invoice Aeroo Report",
    "version": "8.0.1.0.0",
    "category": "Invoicing",
    "website": "https://opensynergy-indonesia.com/",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "report_aeroo",
        "base_amount_to_text",
        "account",
        "hr",
        "account_invoice_line_price_subtotal_gross",
        "account_debt_collection",
    ],
    "data": [
        "data/product_category_data.xml",
        "data/decimal_precision_data.xml",
        "reports/account_proforma_invoice.xml",
        "reports/account_debt_collection_handling.xml",
    ],
}
