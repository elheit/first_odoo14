from odoo import http

class HospitalController(http.Controller):

     @http.route("/hospital/" , website=True)
     def display_patients(self , **kw):
         
         patients = http.request.env['hospital.patient'].search([])
         return http.request.render('om_hospital.hospital_patients',{
           'patients' : patients
         })
         
     @http.route('/hospital/<model("hospital.patient"):patient>/' , website=True)
     def display_patient_details(self , patient):
     
       return http.request.render("om_hospital.hospital_patients_details" , {
          'patient':patient
       })