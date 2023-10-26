from odoo import models , fields , api 
import logging


_logger = logging.getLogger(__name__)

class InheritedModel(models.Model):

   _inherit = ["test_model" ]
   #_name = "inherited.model"
  # property_ids = fields.One2many("estate.property.type","salesperson",string="Property Ids")
   
   
   
   
   
   def action_sold(self):
   
       _logger.warning("\n \n \n \n I4M her ############################# \n \n \n \n"  )
       move = self.env['account.move'].create({
       'partner_id': self.env['test_model'].browse('buyer') ,
       'move_type': 'out_invoice',
       'journal_id':0,
       "line_ids": [
                (
                    0,
                    0,
                    {
                        "sellPrice6": self.selling_price*0.6,
                    },
                    {
                        "administrative fees": self.selling_price + 100.00,
                    },
                )
            ],
       })
        
       return super(InheritedModel,self)