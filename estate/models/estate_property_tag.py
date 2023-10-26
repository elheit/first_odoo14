from odoo import models , fields

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = "applicattion estate_property_tag description"
    _order = "name"
    name =  fields.Char(string="Tag")
    color = fields.Integer(string="Color")
    
    
    
    _sql_constraints = [
       ('unique_tag' , 'unique(name)' , 'the tag name must be unique')
    ]