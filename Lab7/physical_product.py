from product import Product


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