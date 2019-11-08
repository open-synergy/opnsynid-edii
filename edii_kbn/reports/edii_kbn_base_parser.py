# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp.report import report_sxw


class EDIKBNBaseParser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(EDIKBNBaseParser, self).__init__(cr, uid, name, context)
        self.total = 0
        self.context = context
        self.localcontext.update({
            "get_terbilang": self._get_terbilang,
            "get_product_categ": self._get_product_categ,
            "nourut": self._no_urut
        })

    def _get_terbilang(self, value):
        obj_amount2text = self.pool.get("base.amount_to_text")
        obj_res_lang = self.pool.get("res.lang")
        obj_res_currency = self.pool.get("res.currency")
        criteria_lang = [("code", "=", "en_US")]
        criteria_curr = [("name", "=", "IDR")]

        lang_id = obj_res_lang.search(self.cr, self.uid, criteria_lang)
        lang = obj_res_lang.browse(self.cr, self.uid, lang_id)

        currency_id = obj_res_currency.search(self.cr, self.uid, criteria_curr)
        currency = obj_res_currency.browse(self.cr, self.uid, currency_id)

        if currency:
            result = obj_amount2text.get(
                self.cr, self.uid, value, currency, lang)
        else:
            result = "-"
        return result

    def _get_product_categ(self, *value):
        list_data = []
        obj_ir_model_data = self.pool.get("ir.model.data")
        for data in value:
            xml_id = obj_ir_model_data.get_object_reference(
                self.cr, self.uid, "edii_kbn", data)
            result = xml_id and xml_id[1] or False
            if result:
                list_data.append(result)
        return list_data

    def _no_urut(self, value):
        self.total += value
        return self.total
