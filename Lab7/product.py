class Product:

    def __init__(self, ID, name, price, stock):
        self.__ID = ID
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, stock):
        self.__stock = stock

    def display_information(self):
        return {"ID": self.__ID, 
                "Name": self.__name,
                "Price": self.__price,
                "Stock": self.__stock}