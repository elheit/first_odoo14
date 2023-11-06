# -*- coding: utf-8 -*-
from odoo import api, fields, models
from lxml import etree 


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
 

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    appointment_count = fields.Integer(string='Appointment', compute='get_appointment_count')
    appointment_ids = fields.One2many('hospital.appointment','patient_id',string="Appointments")
 
    def get_appointment_count(self):
        for patient in self:
           count = self.env['hospital.appointment'].search_count([('patient_id', '=', patient.id)])
           patient.appointment_count = count
      


    """@api.model
    def fields_view_get(self, view_id=None, view_type='form',
                        toolbar=False, submenu=False):
        res = super(HospitalPatient, self).fields_view_get(
            view_id=view_id, view_type=view_type,
            toolbar=toolbar, submenu=submenu)

        records = self.env['hospital.patient'].search([])

        for rec in records:
                # in this case testing for admin but in the work task it is inverse
                if(rec.appointment_count > 0 and self.env.user.has_group("sales_team.group_sale_manager")):
                    root = etree.fromstring(res['arch'])
                    root.set('create', 'false')
                    root.set('edit', 'false')
                    root.set('delete', 'false')
                    res['arch'] = etree.tostring(root)
                    break

        return res"""

 
  
       