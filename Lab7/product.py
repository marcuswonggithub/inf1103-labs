from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, ID, name, price, stock):
        self._ID = ID
        self._name = name
        self._price = price
        self._stock = stock

    def update_stock(self, stock):
        self._stock = stock

    def display_information(self):
        return {
            "ID": self._ID,
            "Name": self._name,
            "Price": self._price,
            "Stock": self._stock,
        }

    @abstractmethod
    def get_fulfilment_info(self):
        pass


class PhysicalProduct(Product):
    def __init__(self, ID, name, price, stock, weight):
        super().__init__(ID, name, price, stock)
        self._weight = weight

    def display_information(self):
        details = super().display_information()
        details["Weight"] = self._weight
        return details

    def get_fulfilment_info(self):
        return f"{self._name} requires physical shipping."


class DigitalProduct(Product):
    def __init__(self, ID, name, price, stock, download_size):
        super().__init__(ID, name, price, stock)
        self._download_size = download_size

    def display_information(self):
        details = super().display_information()
        details["Download_Size"] = self._download_size
        return details

    def get_fulfilment_info(self):
        return f"{self._name} is delivered digitally through a download."


if __name__ == "__main__":
    physical = PhysicalProduct("P1000", "Laptop", 30.0, 10, 2.5)
    digital = DigitalProduct("D1000", "E-book", 15.0, 100, 5)

    print(physical.display_information())
    print(physical.get_fulfilment_info())

    print(digital.display_information())
    print(digital.get_fulfilment_info())

    physical.update_stock(20)
    print(physical.display_information())

    # Test that Product cannot be instantiated directly.
    try:
        generic = Product("P0000", "Generic", 10.0, 1)
    except TypeError as error:
        print(f"Cannot create Product: {error}")