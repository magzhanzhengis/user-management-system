class UserManager:
    def __init__(self):
        self.users = {}
        self.current_id = 1

    def addUser(self, name):
        user_id = self.current_id
        self.users[user_id] = name
        self.current_id += 1
        return user_id

    def getUser(self, user_id):
        return self.users.get(user_id, None)

    def deleteUser(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False

    def findUserByName(self, name):
        return [user_id for user_id, user_name in self.users.items() if user_name == name]

# Example usage
if __name__ == "__main__":
    userManager = UserManager()

    id1 = userManager.addUser("Jarasar")
    id2 = userManager.addUser("Adil")
    id3 = userManager.addUser("Jarasar")

    print(userManager.getUser(id1))  # Should print "Jarasar"
    print(userManager.getUser(id2))  # Should print "Adil"
    print(userManager.getUser(999))  # Should print None

    print(userManager.findUserByName("Jarasar"))  # Should print [id1, id3]
    print(userManager.findUserByName("Baha"))  # Should print []

    print(userManager.deleteUser(id2))  # Should print True
    print(userManager.deleteUser(999))  # Should print False

    print(userManager.getUser(id2))  # Should print None


