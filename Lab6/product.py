class Product:

    def __init__(self, ID, name, price, stock):
        self.__ID = ID
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, stock):
        self.__stock = stock

    def display_information(self):
        return f'''ID : {self.__ID}
Name: {self.__name}
Price: {self.__price}
Stock: {self.__stock}
'''

product1 = Product("P001", "Laptop", 1200.00, 15) # creating product from Product class, via init
print(product1.display_information())