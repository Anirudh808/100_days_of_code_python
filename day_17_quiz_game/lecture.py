class User:

    def __init__(self, id, name):
        # Attributes: are the variables the object has.
        # used to set attributes while initializing an object.
        print("A new user is being created...")
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        print(f"{self.name} is now following {user.name}")
        user.followers += 1
        self.following += 1


user1 = User("001", "Anirudh")
print(user1.name)

user2 = User("002", "Anjela")
print(user2.name)

print(f"{user1.name} followers: ", user1.followers)
print(f"{user2.name} following: ", user2.following)
user2.follow(user1)
print(f"{user1.name} followers: ", user1.followers)
print(f"{user2.name} following: ", user2.following)


