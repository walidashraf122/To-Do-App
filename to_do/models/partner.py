from odoo import models,fields

class Partner(models.Model):
    _name = 'partner'

    name = fields.Char('Name')

    to_do_ids = fields.One2many('todo.task','assign_to')
