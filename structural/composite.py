from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

    @abstractmethod
    def add(self, component) -> None:
        pass

    @abstractmethod
    def remove(self, component) -> None:
        pass

    @abstractmethod
    def is_composite(self) -> bool:
        pass

class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"

    def add(self, component) -> None:
        raise Exception("Cannot add to a leaf")

    def remove(self, component) -> None:
        raise Exception("Cannot remove from a leaf")

    def is_composite(self) -> bool:
        return False

class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []

    def operation(self) -> str:
        results = ["Composite("]
        for child in self._children:
            results.append(child.operation())
        results.append(")")
        return " + ".join(results)

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def is_composite(self) -> bool:
        return True

def main():
    # Create a tree structure
    tree = Composite()
    
    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print(f"Client: Now I've got a composite tree:\n{tree.operation()}\n")

if __name__ == "__main__":
    main()