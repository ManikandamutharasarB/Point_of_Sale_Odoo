from odoo import api,fields,models

class OnlinePOSproductIDView(models.TransientModel):
    _name = "online.pos.wizard"
    _description = "Online POS Wizard"        
    
    
    
    #inventory_view_wizard=fields.One2many('online.pos.inventory','inventory_view',String='inventory_view_wizard')
    
    product_id=fields.Integer(String='product_id',required=True)
    product_name=fields.Char(String='product_name',required=True)
    price=fields.Integer(String='price',required=True)
    gst=fields.Integer(String='GST',required=True)
    set_product_image=fields.Binary(String='set_product_image',required=True)
    quantity=fields.Integer(String='quantity',required=True)
    
    _sql_constraints=[('unique_product_id','unique(product_id)','This Product ID already exists')]
    _order='product_id asc'
    
    
        