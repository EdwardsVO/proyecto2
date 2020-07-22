from MenuItem import MenuItem

class DrinkItem(MenuItem):
    def __init__(self,  food_name, food_type, food_price, drink_presentation, item_buy):
        super().__init__(food_name, food_type, food_price, item_buy)
        self.drink_presentation = drink_presentation