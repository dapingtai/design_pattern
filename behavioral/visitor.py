from abc import ABC, abstractmethod
from typing import List

# Visitor Interface
class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot) -> None:
        pass

    @abstractmethod
    def visit_circle(self, circle) -> None:
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle) -> None:
        pass

# Element Interface
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass

# Concrete Elements
class Dot(Shape):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_dot(self)

class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int):
        self.x = x
        self.y = y
        self.radius = radius

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_rectangle(self)

# Concrete Visitor
class XMLExportVisitor(Visitor):
    def visit_dot(self, dot) -> None:
        print(f'<dot>\n\t<x>{dot.x}</x>\n\t<y>{dot.y}</y>\n</dot>')

    def visit_circle(self, circle) -> None:
        print(f'<circle>\n\t<x>{circle.x}</x>\n\t<y>{circle.y}</y>\n\t<radius>{circle.radius}</radius>\n</circle>')

    def visit_rectangle(self, rectangle) -> None:
        print(f'<rectangle>\n\t<x>{rectangle.x}</x>\n\t<y>{rectangle.y}</y>\n\t<width>{rectangle.width}</width>\n\t<height>{rectangle.height}</height>\n</rectangle>')

def main():
    # Create shapes
    shapes: List[Shape] = [
        Dot(1, 2),
        Circle(3, 4, 5),
        Rectangle(6, 7, 8, 9)
    ]

    # Create visitor
    visitor = XMLExportVisitor()

    # Export all shapes to XML
    print("Exporting shapes to XML:")
    for shape in shapes:
        shape.accept(visitor)

if __name__ == "__main__":
    main()