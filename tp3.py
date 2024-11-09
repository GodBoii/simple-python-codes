class ClothStore:
    def __init__(self):
        self.clothing_prices = {
            "jeans": 900,
            "shirts": 500,
            "kurti": 200
        }

    def display_prices(self):
        print("Clothing Prices (in INR):")
        for item, price in self.clothing_prices.items():
            print(f"{item.capitalize()}: ₹{price}")

if __name__ == "__main__":
    my_store = ClothStore()
    my_store.display_prices()