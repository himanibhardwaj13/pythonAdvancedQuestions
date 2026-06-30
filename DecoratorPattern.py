def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Log: Executing {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
    
@log_decorator
def secure_door(action):
    print(f"Door action: {action}")
    
secure_door("LOCK")
