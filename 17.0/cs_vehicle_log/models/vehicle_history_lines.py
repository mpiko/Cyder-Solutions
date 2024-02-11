from odoo import models, api, fields
from odoo.exceptions import ValidationError


class VehicleHistoryLines(models.Model):
    _name = 'vehicle.history.lines'
    _description = 'Vehicle History Lines'

    date = fields.Date(string='Date')
    od_start_read = fields.Integer(string='Odometer Start Readings')
    task_id = fields.Integer(string='Task')
    # log_id = fields.Many2one('vehicle.log', string='Vehicle Log')
    yearly_distance = fields.Float(string='Yearly Distance', compute='_compute_yearly_distance')


    # @api.onchange('date')
    # def _check_date(self):
    #     for rec in self:
    #         if rec.date.month != 7 or rec.date.day != 1:
    #             raise ValidationError("Date must be July 1st.")

    def _compute_yearly_distance(self):
        for rec in self:
            previous_recs = self.search([ ('date', '<', rec.date), ('id', '!=', rec.id)], order='date DESC', limit=1)

            if previous_recs:
                previous_rec = previous_recs[0]
                rec.yearly_distance = rec.od_start_read - previous_rec.od_start_read
            else:
                rec.yearly_distance = 0.0




