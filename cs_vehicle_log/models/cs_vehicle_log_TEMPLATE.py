# -*- coding: utf-8 -*-

#     INSTRUCTION
#     TITLENAME is the display name
#     TITLE is the technical name
#     Hint: When replacing, do TITLENAME first then do TITLE
#     Set the correct parent and sequence number for the menu
#     
#     Model
#     Do the same for the model in the py file
#     Rename and add import to the __init__.py
#     
#     Security
#     Replace TITLE and add to the security file
#       access.cs_vehicle_log.TITLE,access_cs_vehicle_log.TITLE,cs_vehicle_log.model_cs_vehicle_log_TITLE,base.group_user,1,1,1,1
#     
#     Add the view to the __manifest__.py
#                                                                                                                       

from odoo import api, fields, models
class Cs_vehicle_logTITLE(models.Model):
    _name = "cs_vehicle_log.TITLE"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Cs_vehicle_log TITLENAME"

    name = fields.Char('TITLENAME Name')
    active = fields.Boolean(default=True)
