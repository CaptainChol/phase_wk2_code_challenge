class  Restaurant:
    def __init__(self,name="A Chinese Restaurant"):
        self.name = name
        
    def restaurant_name(self):
        return self.name    

    # def set_rest(self, name):
    #     self.name=name
        
    restaurant = property(restaurant_name) 


restaurant = Restaurant()
print(restaurant.restaurant_name())     