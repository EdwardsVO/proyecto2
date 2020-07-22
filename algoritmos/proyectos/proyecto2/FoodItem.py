from MenuItem import MenuItem

class FoodItem(MenuItem):
    def __init__(self,  food_name, food_type, food_price, food_presentation, item_buy):
        super().__init__(food_name, food_type, food_price, item_buy)
        self.food_presentation = food_presentation