from odoo import models , fields ,api
from dateutil import relativedelta
from . import estate_property_type


class EstatePropertyOffer(models.Model):
   _name = "estate.property.offer"
   _description = "description pour estate.property.offer model"
   #_order = "price desc"
   price = fields.Float(string="Price")
   status = fields.Selection([('accepted' , 'Accepted'),('refused' , 'Refused')] , string="Status" )
   partner_id = fields.Many2one('res.partner', string="Partners" , required=True )
   property_id = fields.Many2one ('estate.property.type', required=True)
   validity = fields.Integer(string="Validity (days)" , default=7)
   date_deadline = fields.Date(string="Date Deadline", inverse="_inverse_date_deadline" )
   
   
   _sql_constraints = [
       ('price_positive' , 'check(price > -1.00) ' , 'the offer price must be positive')
    ]
   
   
   
   
   @api.depends('validity' )
   def _inverse_date_deadline(self):
       for item in self:
        item.date_deadline = item.create_date + relativedelta.relativedelta(days=item.validity)
   
   
   def action_accept(self):
        for record in self:
          record.status = 'accepted'
        return True
        
   def action_refused(self):
        for record in self:
           record.status = 'refused'
        return True
   
   
   
   
   
   
   
   
   
   
