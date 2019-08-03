# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StudendRecords(models.Model):
    _name = "student.student"
    
    student_class = fields.Many2one('student.class',string='Class')
    student_shift = fields.Many2one('student.shift',string='Shift')
    first_name = fields.Char(string='First Name', required=True)
    acedmic_year = fields.Char(string='Acedmic Year', required=True)
    admission_number = fields.Integer(string='Admission Number', required=True)
    admission_date = fields.Date(string="Admission Date")
    shift = fields.Char(string='Shift', required=True)
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name', required=True)
    student_father_name = fields.Char(string='Father Name', required=True)
    student_mother_name = fields.Char(string='Mother Name', required=True)
    photo = fields.Binary(string='Photo')
    student_age = fields.Integer(string='Age')
    student_dob = fields.Date(string="Date of Birth")
    student_gender = fields.Selection([('m','Male'),('f','Female'),('o','Other')],string='Gender')
    student_blood_group = fields.Selection(
       [('A+','A+ve'), ('B+','B+ve'), ('O+','O+ve'), ('AB+','AB+ve'),
        ('A-','A-ve'), ('B-','B-ve'), ('O-','O-ve'), ('AB-','AB-ve')],
        string='Blood Group')
    
    nationality = fields.Many2one('res.country', string='Nationality')
    student_houseno = fields.Char(string='House no',required=True)
    student_streetno = fields.Integer(string='Street no',required=True)
    student_locality = fields.Char(string='Locality',required=True)
    student_city = fields.Char(string='City',required=True)
    student_pincode = fields.Integer(string='Pin code',required=True)
    student_state = fields.Char(string='State',required=True)
    contact_number = fields.Char(string='Contact Number', required=True)
    alternate_contact_number = fields.Char(string='Alternate Contact Number')
    
    
class ClassRoom(models.Model):
    _name = "student.class"
    _rec_name = "class_name"
    
    student1 = fields.One2many('student.student','student_class','Student')
    class_name = fields.Char(string='Class', required=True)
    class_medium = fields.Char(string='Medium', required=True)
    class_shift = fields.Many2one('student.shift', string='Shift', required=True)
    class_teacher = fields.Char(string='Teacher name', required=True)
    class_section = fields.Char(string='Section', required=True)
    number_of_subjects = fields.Integer(string='Total Subject', required=True)

    
class Shift(models.Model):
    _name = "student.shift"
    _rec_name = "shift_name"
    
    shift_name = fields.Char(string='Shift Name',required=True)
    shift_timing = fields.Char(string='Shift Timing',required=True)
    
class Teacher(models.Model):
    _name = "student.teacher"
    _rec_name = "teacher_name"
    
    teacher_name = fields.Char(string='Teacher Name',required=True)
    photo = fields.Binary(string='Photo')
    teacher_id = fields.Char(string='Teacher ID',required=True)
    teacher_qualification = fields.Char(string='Qualification',required=True)
    teacher_houseno = fields.Char(string='House no',required=True)
    teacher_streetno = fields.Integer(string='Street no',required=True)
    teacher_locality = fields.Char(string='Locality',required=True)
    teacher_city = fields.Char(string='City',required=True)
    teacher_pincode = fields.Integer(string='Pin code',required=True)
    teacher_state = fields.Char(string='State',required=True)
    contact_number = fields.Char(string='Contact Number', required=True)
    teacher_shift = fields.Many2one('student.shift',string='Shift')

class Subject(models.Model):
    _name = "student.subject"
    _rec_name = "subject"
    
    subject = fields.Char(string='Subject',required=True)
    marks = fields.Integer(string='Marks',default='100')

class Detail(models.Model):
    _name = "student.detail"
    
    class_detail = fields.Many2one('student.class',string='Class')
    subject = fields.Many2one('student.subject',string='Subject')
    teacher = fields.Many2one('student.teacher',string='Teacher')
    shift = fields.Many2one('student.shift',string='Shift')