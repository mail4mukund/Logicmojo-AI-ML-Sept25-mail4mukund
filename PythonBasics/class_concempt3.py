class MyClass:
    count = 0  # Class variable to keep track of the number of instance
    @classmethod
    def increment_count(cls):
        cls.count += 1
        return cls.count
    
MyClass.increment_count()
MyClass.increment_count()

print(MyClass.count)  # Output: 1