# -*- coding: utf-8 -*-

from odoo import api, fields, models


class OnlinePOSPayment(models.Model):
    
    _name = "online.pos.payment"
    _description = "Online POS Payment"
    _inherit="online.pos.product.details"
    

    grand_total = fields.Float(String='grand_total')
    cash = fields.Float(String='cash')
    upi_payment = fields.Char(String='upi_payment')
    card_payment = fields.Selection([('credit', 'Credit'), ('debit', 'Debit')])
    card_bank = fields.Selection([('sbi', 'State Bank of India'), ('axis', 'Axis Bank'), ('kvb', 'Karur Vysya Bank'), ('iob', 'Indian Overseas Bank'), ('cb', 'Canara Bank'), ('icici', 'ICICI Bank'), ('hdfc', 'HDFC Bank')])
    card_holder = fields.Char(String='card_holder')
    card_number = fields.Integer(String='card_number')
    
    #get_payment_record=Many2one('online.pos.product.details','payment_record',String='get_payment_record')
    
    def online_payment(self):
        print('upi_payment')
   
