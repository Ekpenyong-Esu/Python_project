class Singleton:
    _instance = None

    def __init__(self):
        if not Singleton._instance:
            print("Creating Singleton instance")
        else:
            print("Singleton instance already exists")

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

# Example usage:
singleton_instance1 = Singleton.get_instance()

print("  ")

singleton_instance2 = Singleton.get_instance()

print(singleton_instance1 is singleton_instance2)  # This should print True
