class Product:

    def __init__(self, ID, name, price, stock):
        self._ID = ID
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, stock):
        self._stock = stock

    def display_information(self):
        return {"ID": self._ID, 
                "Name": self._name,
                "Price": self._price,
                "Stock": self._stock}

class PhysicalProduct(Product):

    def __init__(self, ID, name, price, stock, weight):
        super().__init__(ID, name, price, stock)
        self._weight = weight

    def display_information(self):
        details = super().display_information()
        details["Weight"] = self._weight
        return details

class DigitalProduct(Product):

    def __init__(self,ID, name, price, stock, download_size):
        super().__init__(ID, name, price, stock)
        self._download_size = download_size

    def display_information(self):
        details = super().display_information()
        details["File Size"] = self._file_size
        return details


physical = PhysicalProduct("P1000", "Laptop", 30.0, 10, 2.5)

print(physical.display_information())

physical.update_stock(20)
print(physical.display_information())    
