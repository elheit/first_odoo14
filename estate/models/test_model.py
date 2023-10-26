from odoo import models , fields , api 
from odoo.exceptions import AccessError , ValidationError




class TestModel(models.Model):
    _name = 'test_model'
    _description = "applicattion test description"
    _order = "id desc"
    title = fields.Char(string='Title',required=True , copy=False)
    postcode = fields.Char(string="Postcode")
    expected_price = fields.Float(string="Expected Price",required=True)
    selling_price = fields.Float()
    description = fields.Text()
    availability_date = fields.Date(default=lambda self: fields.Datetime.now() )
    bedrooms = fields.Integer(string='Bedrooms',default=2)
    post_code = fields.Integer()
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection([('north','North'), ('south','South') , ('east','East') , ('west','West') ])
    states = fields.Selection([('new','New'), ('offer received','Offer Received') , ('offer accepted','Offer Accepted') , ('sold ','SOLD ') ] ,
    default='new' , string="State")
    total_area = fields.Integer(string="Total Area (sqm)" , compute="_compute_total_area")
    status = fields.Selection([('cancaled','Cancaled') , ('sold','Sold')])
    buyer  = fields.Many2one(string="Buyer", comodel_name="res.partner" )




    _sql_constraints = [
       ('price_selling_positive' , 'check(selling_price > -1.00) ' , 'the selling_price must be positive')
    ]
    
    
    
    def unlink(self):
          if(self.states != "new"):            
             raise ValidationError("you can not delete this element")
             
             
          return super(TestModel, self).unlink()
    
    
    
    @api.model
    def create(self,vals):
      vals['states'] = 'offer received'
      return super(TestModel,self).create(vals)
    
    
    @api.depends('living_area' , 'garden_area')
    def _compute_total_area(self):
            self.total_area = self.living_area + self.garden_area
            
    
    
    @api.onchange('garden')
    def onchange_garden(self):
       if(self.garden):
          self.garden_area = 10
          self.garden_orientation = 'north'
       else:
          self.garden_area = None
          self.garden_orientation = None
          
          
    def action_sold(self):
        for record in self:
           if(record.status != "cancaled"):
               record.status = "sold"
           else:
              raise AccessError(message="the property is already cancaled")
           
        return True
        
    def action_cancaled(self):
        for record in self:
           if(record.status != "sold"):
              record.status = "cancaled"
           else:
             raise AccessError(message="the property is already sold")
           
        return True
        
    
    