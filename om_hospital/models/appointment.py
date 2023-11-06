from odoo import models, fields, api,  _
from odoo.exceptions import UserError
import logging


_logger = logging.getLogger(__name__)



class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'

    name = fields.Char(string='Appointment ID', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer('Age', related='patient_id.age')
    notes = fields.Text(string="Registration Note")
    appointment_date = fields.Date(string='Date')
    appointment_datetime = fields.Datetime(string='Date Time')
    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirm'),
            ('done', 'Done'),
            ('cancel', 'Cancelled'),
        ], readonly=True, default='draft')
    
    @api.model
    def create(self, vals):
        for record in self:
            if record.state == "done":
               raise UserError("Cannot create the element with appointment_count greater than 0")
        # overriding the create method to add the sequence
            if vals.get('name', _('New')) == _('New'):
               vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result
        
    def unlink(self):
        for record in self:
            if record.state == "done":
                raise UserError("Custom error message: Cannot delete the element with appointment_count greater than 0")
        return super(HospitalAppointment, self).unlink()
        
            
    def action_set_confirm(self):
       self.state = 'confirm'
       
       
       
    def action_set_done(self):            
        self.state = 'done'
     
        
        




