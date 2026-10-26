class Product:
    __product_id:str
    __name:str
    __price:float
    __stock:int


    def __init__(self,product_id,name,price,stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self,quantity):
        self.__stock = quantity

    def display_information(self):
        print(f"ID: {self.__product_id}\nName: {self.__name}\nPrice: ${self.__price:.2f}\nStock: {self.__stock}")

