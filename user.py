from log_operations import log_operation
from models import User
from storage import Storage

class UserManager:
    def __init__(self):
        user_data = Storage.load_data("users.json")
        self.users = [User(**data) for data in user_data]

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        Storage.save_data("users.json", self.users)
        log_operation(f"Added user: {name} (ID: {user_id})")
    
    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                Storage.save_data("users.json", self.users)
                log_operation(f"Deleted user: {user.name} (ID: {user_id})")
                return True
        log_operation(f"User not found for deletion: {user_id}")
        return False

    def update_user(self, user_id, name):
        for user in self.users:
            if user.user_id == user_id:
                user.name = name
                Storage.save_data("users.json", self.users)
                log_operation(f"Updated user: {user.name} (ID: {user_id})")
                return True
        log_operation(f"User not found for update: {user_id}")
        return False

    def list_users(self):
        for user in self.users:
            print(user)

    def search_user(self, user_id=None, name=None):
        for user in self.users:
            if (user_id and user.user_id == user_id) or (name and user.name == name):
                return user  
        return None

