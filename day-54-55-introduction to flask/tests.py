class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

@is_authenticated
def create_blogpost(user):
    print(f"this is {user.name}' blogpost.")


new_user = User("Jakub")
new_user.is_logged_in = True
create_blogpost(new_user)
