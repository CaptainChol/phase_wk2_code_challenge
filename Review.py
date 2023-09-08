class Review:
    all_reviews=[]
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating=rating
        self.add_reviews()
        
    def add_reviews(self):
        self.all_reviews.append(self)
    
    @classmethod
    def get_all_reviews(cls):
        return cls.all_reviews 
        
    def get_customer(self):
        return self.customer
    
    def get_restaurant(self):
        return self.restaurant
    
    @classmethod
    def customers(cls):
        unique_customers = set()

        for review in cls.all_reviews:
        # will use set data structure as it takes only on argument
         unique_customers.add(review.customer)
        # Returns a **unique** list of all customers who have reviewed a particular restaurant.
        return list(unique_customers)
    
    @classmethod
    def restaurants(cls):
        unique_restaurant = set()

        for review in cls.all_reviews:
            # will use tuple data structure to insert two items restaurant and the rating associated
            unique_restaurant.add((review.restaurant, (review.rating)))
        # Returns a **unique** list of all restaurants a customer has reviewed    
        return list(unique_restaurant)  
    
    @classmethod
    def num_reviews(cls, customer):
        # this class method takes two arguments 
        #  initiated count and assign 0 value              
        total_count = 0
        
        for review in cls.all_reviews:
             if review.customer == customer:
              total_count += review.rating
             else:
                 return "Customer not in the list" 
        # Returns the total number of reviews that a customer has authored
        return total_count    
    @classmethod
    def find_by_name(cls, name):
        for review in cls.all_reviews:
            if review.customer == name:
                return review.customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        fullname = [review.customer for review in cls.all_reviews if review.customer == name]

        if fullname:
            # given a string of a given name, returns an **list** containing all customers with that given name
            return fullname
        else:
            return "no matching name"

    @classmethod
    def average_star_rating(cls):      

      average_rating= sum([review.rating for review in cls.all_reviews])/ len(cls.all_reviews)
     
      return average_rating
        

    

review = Review("Jane Mbuya", "Fourth Street", 8)
review2 = Review("John Doe", "Third Avenue", 9)
review3 = Review("John Doe", "Third Avenue", 9)

# this will call an instance 
print(review.get_all_reviews())
print(review.get_customer())
print(review.get_restaurant())

# this will call a class method 
print(Review.customers())
print(Review.restaurants())
print(Review.num_reviews("John Doe"))
print(Review.find_by_name("John Doe"))
print(Review.find_all_by_given_name("John Doe"))
print(Review.average_star_rating())
