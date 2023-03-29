# Define a decorator function for user authentication
def user_authentication(func):
    def wrapper(*args, **kwargs):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # Check if user is authenticated
        if username == "admin" and password == "1234":
            # Call the original function
            return func(*args, **kwargs)
        else:
            # Error Message
            return "Authentication failed. Access denied."
    return wrapper

# Define a function that requires authentication
@user_authentication
def my_function():
    # This function can only be called by authenticated users
    return "Hello, world!"

result = my_function()
print(result)