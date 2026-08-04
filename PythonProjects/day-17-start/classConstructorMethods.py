class User:
    # initialize or create the starting values for our class
        # the init function will be called EVERYTIME we create as new object from our class
        # self is the actual object being created
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.followers = 0

    # Method must always have a self param so it knows the object that called it
    def update_follower_count(self, user):
        # update the user who I followed count
        user.followers += 1
        # update my follower count
        self.followers += 1


# create an object from our user class and set values
user_1 = User(1,"Big","Daddy")
user_2 = User(2,"Big","Momma")
print(user_1.followers)

# update the follower count via the constructor method
user_1.update_follower_count(user_2) # 1 follower
print(f"User 1 follower count is {user_1.followers}")
print(f"User 2 follower count is {user_2.followers}")

