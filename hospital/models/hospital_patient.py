from odoo import models , fields , api , _
from odoo.exceptions import AccessError , ValidationError




class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], required=True, default='male')
    note = fields.Text(string='Description')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='draft' , string="Status")
    
    responsable_id = fields.Many2one('res.partner', Sstring="Responsable")
    reference = fields.Char(string="reference",required=True , readonly=True , default=_("New"))
    appointement_count = fields.Integer(string="Appointement Count" , compute="_compute_appointement_count" )
    
    def _compute_appointement_count(self):
       for rec in self:
         rec.appointement_count = rec.env['hospital.appointment'].search_count([('patient_id' , '=' , rec.id)])
    
    
    def hospital_patient_action_confirm(self):
        for rec in self:
           rec['state'] = 'confirm'
           
           
    def hospital_patient_action_done(self):
        for rec in self:
           rec['state'] = 'done'
           
    def hospital_patient_action_draft(self):
        for rec in self:
           rec['state'] = 'draft'
           
           
    def hospital_patient_action_cancel(self):
        for rec in self:   
           rec['state'] = 'cancel'
    
    @api.model
    def create(self,vals):
      if not vals.get('note'):
         vals['note'] = "New Patient Created "
      if vals.get('reference' , _("New")) == _("New"):
         vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _("New")
      return super(HospitalPatient,self).create(vals)
    
    
    
    
    
    
    
    
    
    