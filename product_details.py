from odoo import api,fields,models

class OnlinePOSproductID(models.Model):
    _name = "online.pos.product.details"
    _description = "Online POS Product Details"  
    #_inherit = "online.pos.billing"
    #_inherit = "online.pos.payment"
    #_inherits = ['online.pos.billing','online.pos.payment']
   
    name=fields.Many2one(comodel_name='online.pos.customer',required=True)
    grand_total=fields.Float(compute='onchange_grand_total', String='grand_total',required=True)
   
    records=fields.One2many('online.pos.billing','get_record',String='record_one_2_many')
    #payment_record=One2many('online.pos.payment','get_payment_record',String='payment_record')
    
    @api.onchange('name','grand_total','records')
    def onchange_grand_total(self):
        for find_total in self:
            find_total.grand_total = 0
            for find_product_total in find_total.records :
                find_total.grand_total += find_product_total.total
                
#     @api.onchange('records')            
#     def onchange_quantity(self):
#         
#         for calculate_product in self:
#             for calculate_same_item in calculate_product.records:
#                 if calculate_product.product_name == calculate_same_item.product_name:
#                     calculate_product.quantity+=calculate_same_item.quantity
#                     
    def make_payment(self):
        print('make payment in product details')                
                    
                    