from product import Product


class DigitalProduct(Product):
    def __init__(self, ID, name, price, stock, download_size):
        super().__init__(ID, name, price, stock)
        self._download_size = download_size

    def display_information(self):
        details = super().display_information()
        details["Download_size"] = self._download_size
        details["Type"] = "digital"
        return details

    def get_fulfilment_info(self):
        return f"{self._name} is delivered digitally through a download."