from odoo import api, fields, models

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    hide = fields.Boolean(string='Hide', help="Hide quantity and unit price on sales reports")

    @api.model
    def create(self, vals):
        vals['hide'] = self.env['product.template'].search([('id', '=', vals['product_template_id'])]).hide
        res = super(SaleOrderLine, self).create(vals)
        return res



