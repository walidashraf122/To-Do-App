from odoo import models,fields

class ToDo(models.Model):
    _name = 'todo.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    task_name = fields.Char()
    assign_to = fields.Many2one('partner')
    description = fields.Char()
    due_date = fields.Date()
    status = fields.Selection([('new','New'),('in_progress','In Progress'),('completed','Completed')])

    def action_new(self):
        for rec in self:
            rec.status = 'new'

    def action_in_progress(self):
        for rec in self:
            rec.status = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.status = 'completed'