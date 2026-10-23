class Inventory:

    def __init__(self):
        self.storage = {}

    def add_product(self, product_id, product):
        if product_id in self.storage:
            return "Product ID already exists."
        self.storage[product_id] = product


    def search_product(self, product_id):
        if product_id not in self.storage:
            return "Product not found"
        
        return self.storage[product_id]

    def display_all(self):
        all = []
        for product in self.storage.values():
            all.append(product)
        return all