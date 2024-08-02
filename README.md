# User Management System

This is a simple user management system implemented in Python.

## How to Run

1. Make sure you have Python installed. If not, download and install it from [Python.org](https://www.python.org/downloads/).
2. Download the `user_manager.py` file from this repository.
3. Open a command prompt or terminal and navigate to the directory containing `user_manager.py`.
4. Run the script using the following command:
   ```sh
   python user_manager.py
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
