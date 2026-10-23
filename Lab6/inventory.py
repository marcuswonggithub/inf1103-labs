class Inventory:

    def __init__(self):
        self.__storage = {}

    def add_product(self, product_id, product):
        if product_id in self.__storage:
            return "Product ID already exists."
        self.__storage[product_id] = product


    def search_product(self, product_id):
        if product_id not in self.__storagestorage:
            return "Product not found"
        
        return self.__storage[product_id]

    def display_all(self):
        all = []
        for product in self.__storage.values():
            all.append(product)
        return all