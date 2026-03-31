def check_admin(func):
    def wrapper(user):
        if user["role"] != "admin":
            return "chal hatt"
        return func(user)
    return wrapper
        

@check_admin
def delete_user(user):
    return f"User {user['name']} deleted!"


# test users
admin = {"name": "Rahul", "role": "admin"}
normal = {"name": "Priya", "role": "user"}
manager = {"name": "Sam",  "role": "manager"}

print(delete_user(admin))    
print(delete_user(normal))   
print(delete_user(manager))