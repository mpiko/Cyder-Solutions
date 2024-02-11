from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    hide = fields.Boolean(string='Hide Qty and Unit Cost', help="Hide quantity and unit price on sales reports")

