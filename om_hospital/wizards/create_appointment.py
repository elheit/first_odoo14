# -*- coding: utf-8 -*-

from odoo import models, fields


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'Create Appointment Wizard'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Date(string='Appointement date')
    
    
    def action_create_appointment(self):
      vals={
         'name':self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New'),
         'patient_id':self.patient_id.id,
         'appointment_date':self.appointment_date
      }
      self.env['hospital.appointment'].create(vals)
    