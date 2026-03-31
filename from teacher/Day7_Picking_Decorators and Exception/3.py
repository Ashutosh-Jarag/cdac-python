def to_uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@to_uppercase
def get_message():
    return "hello world"
    

print(get_message())