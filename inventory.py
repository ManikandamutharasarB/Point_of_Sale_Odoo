from odoo import api,fields,models

class OnlinePOSproductID(models.TransientModel):
    _name = "online.pos.inventory"
    _description = "Online POS Inventory"        
    
    product_id=fields.Integer(String='product_id',required=True)
    name=fields.Char(String='name',required=True)
    price=fields.Integer(String='price',required=True)
    gst=fields.Integer(String='GST',required=True)
    set_product_image=fields.Binary(String='set_product_image',max_width=10,max_height=10)
    quantity=fields.Integer(String='quantity',required=True)
    
    state=fields.Selection([('godown','Godown'),('selling floor','Selling Floor')],String="Status",default='godown')
    
    #inventory_view=fields.Many2one('online.pos.wizard','inventory_view_wizard',String='inventory_view')
    
    #def action_product_details(self):
       
     #  vals={
      #          'product_id': self.product_id.product_id,
       #         'name': self.name.product_name,
        #        'price': self.price.price,
         #       'gst': self.gst.gst,
          #      'set_product_image': self.set_product_image.set_product_image,
           #     'quantity': self.quantity.quantity           
            #}
   
            
    
   