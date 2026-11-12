from abc import ABC,abstractmethod

#assocation object
class Supplier(ABC):
    def __init__(self,supplier_id:str,name:str,contact_email:str):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email
    
 