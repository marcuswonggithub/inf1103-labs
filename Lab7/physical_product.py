from product import Product
from can_be_shipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, ID, name, price, stock, weight):
        super().__init__(ID, name, price, stock)
        self._weight = weight

    def display_information(self):
        details = super().display_information()
        details["Weight"] = self._weight
        details["Type"] = "physical"
        return details

    def get_fulfilment_info(self):
        return f"{self._name} requires physical shipping."

    def calculate_shipping_cost(self):
        cost = self._weight * 8
        return cost