from abc import ABC,abstractmethod

#assocation object
class Supplier(ABC):
    def __init__(self,supplier_id,name,contact_email):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email
    
 