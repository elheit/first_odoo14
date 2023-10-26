from odoo import models , fields , api 

class InheritedModel(models.Model):

   _inherit = "res.users"
   property_ids = fields.One2many("estate.property.type","salesperson",string="Property Ids")