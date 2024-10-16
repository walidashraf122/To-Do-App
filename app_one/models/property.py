from odoo import models,fields,api

from encodings.punycode import digits
from server.odoo.api import constrains
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name ='property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    description = fields.Text(racking=1)
    postcode = fields.Char(racking=1)
    date_availability = fields.Date(tracking=1)
    expected_price = fields.Float(required=True)
    diff = fields.Float(compute='_compute_diff')
    selling_price = fields.Float(required=True)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),('south','South'),('east','East'),('west','West')
    ],default ='north')

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    owner_address = fields.Char(related='owner_id.address')
    owner_phone = fields.Char(related='owner_id.phone')

    state = fields.Selection([('draft','Draft'),
                              ('pending','Pending'),
                              ('sold','Sold'),
                              ], default='draft')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'The name must be unique.'),]



    @api.depends('expected_price','selling_price','owner_id.phone')
    def _compute_diff(self):
        for rec in self:
            print('from customer')
            rec.diff = rec.expected_price - rec.selling_price


    @api.onchange('expected_price')
    def onchange_expected_price(self):
        for rec in self:
            print('from expected price')



    def action_draft(self):
        for rec in self:
            print('inside draft action')
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            print('inside pending action')
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            print('inside sold action')
            rec.state = 'sold'



    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError('Please add valid number of bedrooms')


    # @api.model_create_multi
    # def create(self,vals):
    #     res = super(Property,self).create(vals)
    #     print()
    #     return res
    #
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super(Property, self)._search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     print()
    #     return res
    #
    # def write(self, vals):
    #     res = super(Property, self).write(vals)
    #     print()
    #     return res
    #
    #
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print()
    #     return res