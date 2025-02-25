from abc import ABC, abstractmethod

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Operation implemented."

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB: Operation implemented."

class Abstraction:
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self):
        return f"Abstraction: Base operation with:\n{self.implementation.operation_implementation()}"

class RefinedAbstraction(Abstraction):
    def operation(self):
        return f"RefinedAbstraction: Extended operation with:\n{self.implementation.operation_implementation()}"

def main():
    implementation_a = ConcreteImplementationA()
    implementation_b = ConcreteImplementationB()

    abstraction = Abstraction(implementation_a)
    print(abstraction.operation())

    refined = RefinedAbstraction(implementation_b)
    print(refined.operation())

if __name__ == "__main__":
    main()