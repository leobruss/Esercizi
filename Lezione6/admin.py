from lezione6_obbligatori import User
from lezione6_obbligatori import Admin
from lezione6_obbligatori import Privileges

print("\n")
user1 = Admin("Leonardo", "Brussani", 19, "Male", 3278242560, 1, ["can add post", "can delete post", "can ban user"])
Privileges.show_privileges(user1)