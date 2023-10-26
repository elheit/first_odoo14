from odoo import models , fields , api
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare
import logging


_logger = logging.getLogger(__name__)

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "applicattion estate property type description"
    _order = "name"
    name = fields.Char(required=True , string="Name")
    description = fields.Text()
    property_type = fields.Char(required = True)
    buyer  = fields.Many2one(string="Buyer", comodel_name="res.partner" )
    salesperson  =  fields.Many2one(string="SelePerson", comodel_name="res.users" , default=lambda self: self.env.user)
    tags = fields.Many2many('estate.property.tag' , string="Tags")
    offer_ids = fields.One2many("estate.property.offer" , "property_id" , string="Offers")
    best_offer = fields.Float(compute = "_compute_best_price")
    expected_price = fields.Float(string="Expected Price",required=True)
    selling_price = fields.Float(string="Selling Price")
    sequence = fields.Integer('Sequence', default=1)
    states = fields.Selection([('new','New'), ('offer received','Offer Received') , ('offer accepted','Offer Accepted') , ('sold ','SOLD ') ] )

    
    _sql_constraints = [
      # ('unique_property_type' , 'unique(property_type_id)' , 'the property type id must be unique'),
       ('unique_property_name' , 'unique(name)' , 'the property name must be unique'),
    ]
    
    
    
    @api.model
    def create(self,vals):
      #self.env['res.partner'].browse(vals['price'])
      _logger.warning("\n \n \n \n I4M her ############################# "+vals['name'] +"\n \n \n \n"  )
      
      return super(EstatePropertyType,self).create(vals)
      
      
      
      
    @api.depends('offer_ids.price')
    def _compute_best_price(self):
            self.best_offer = max(self.offer_ids.mapped('price') , default = 0.0) 

    
    @api.constrains('expected_price' , 'selling_price')
    def _check_price(self):
      for record in self:
         if ( float_compare(record.selling_price , (record.expected_price * 0.9) , precision_rounding = 1) == -1):
            raise ValidationError("the selling Price must be 90% of the Excpected Price")