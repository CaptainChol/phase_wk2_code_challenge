class  Restaurant:
    def __init__(self,name="A Chinese Restaurant"):
        self.name = name
        
    def restaurant_name(self):
        return self.name    

    # def set_rest(self, name):
    #     self.name=name
        
    Restaurant = property(restaurant_name) 


Restaurant = Restaurant()
print(Restaurant.restaurant_name())     