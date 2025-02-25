from abc import ABC, abstractmethod

class Creator(ABC):
    """
    Creator class declares the factory method that returns new product objects.
    """
    
    @abstractmethod
    def factory_method(self):
        """
        Factory Method to be implemented by concrete creators.
        """
        pass

    def some_operation(self) -> str:
        """
        Core business logic that uses the factory method.
        """
        product = self.factory_method()
        result = f"Creator: Working with {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    """
    Concrete Creator override the factory method to change the resulting product's type.
    """
    
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

class Product(ABC):
    """
    Product interface declares operations that all concrete products must implement.
    """
    
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Result of ConcreteProduct1"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Result of ConcreteProduct2"

def main():
    """Client code"""
    print("App: Launched with ConcreteCreator1")
    creator1 = ConcreteCreator1()
    print(creator1.some_operation())
    
    print("\nApp: Launched with ConcreteCreator2")
    creator2 = ConcreteCreator2()
    print(creator2.some_operation())

if __name__ == "__main__":
    main()