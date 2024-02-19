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
#       access.mx_elearning_plus.TITLE,access_mx_elearning_plus.TITLE,mx_elearning_plus.model_mx_elearning_plus_TITLE,base.group_user,1,1,1,1
#     
#     Add the view to the __manifest__.py
#                                                                                                                       

from odoo import api, fields, models
class Mx_elearning_plusTITLE(models.Model):
    _name = "mx_elearning_plus.TITLE"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Mx_elearning_plus TITLENAME"

    name = fields.Char('TITLENAME Name')
    active = fields.Boolean(default=True)
