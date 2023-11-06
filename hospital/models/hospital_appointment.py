from odoo import models, fields, api,  _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    
    
    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    #doctor_id = fields.Many2one('hospital.doctor', string='Doctor')
    patient_age = fields.Integer('Age',related="patient_id.age")
    notes = fields.Text(string="Registration Note")
    #doctor_note = fields.Text(string="Note", track_visibility='onchange')
    appointment_date = fields.Date(string='Date')
    
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, default='draft')
        
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], required=True)

    
    def hospital_appointment_action_confirm(self):
        for rec in self:
           rec['state'] = 'confirm'
           
           
    def hospital_appointment_action_done(self):
        for rec in self:
           rec['state'] = 'done'
           
    def hospital_appointment_action_draft(self):
        for rec in self:
           rec['state'] = 'draft'
           
           
    def hospital_appointment_action_cancel(self):
        for rec in self:   
           rec['state'] = 'cancel'
           
    
    
    @api.model
    def create(self,vals):
      if vals.get('name' , _("New")) == _("New"):
         vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _("New")
      return super(HospitalAppointment,self).create(vals)
           
    
    @api.onchange('patient_id')
    def onchange_patient_id(self):
      for rec in self:
        if rec.patient_id:
          if rec.patient_id.gender:
              rec.gender = rec.patient_id.gender
           
        else:
          rec.gender = ""
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           