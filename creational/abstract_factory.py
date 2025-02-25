"""
Abstract Factory Pattern Implementation

抽象工廠模式允許我們創建一系列相關的對象，而無需指定它們的具體類。
這個例子展示了如何使用抽象工廠模式來創建不同風格的家具（現代和傳統）。
"""

from abc import ABC, abstractmethod

# Abstract Product Classes
class Chair(ABC):
    @abstractmethod
    def sit(self):
        pass

class Table(ABC):
    @abstractmethod
    def place_item(self):
        pass

# Concrete Product Classes - Modern Style
class ModernChair(Chair):
    def sit(self):
        return "Sitting on a modern chair"

class ModernTable(Table):
    def place_item(self):
        return "Placing item on a modern table"

# Concrete Product Classes - Traditional Style
class TraditionalChair(Chair):
    def sit(self):
        return "Sitting on a traditional chair"

class TraditionalTable(Table):
    def place_item(self):
        return "Placing item on a traditional table"

# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_table(self) -> Table:
        pass

# Concrete Factories
class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()

class TraditionalFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return TraditionalChair()

    def create_table(self) -> Table:
        return TraditionalTable()

# Client Code
def client_code(factory: FurnitureFactory):
    chair = factory.create_chair()
    table = factory.create_table()
    
    print(chair.sit())
    print(table.place_item())

# Usage Example
if __name__ == "__main__":
    print("Testing Modern Furniture Factory:")
    client_code(ModernFurnitureFactory())
    
    print("\nTesting Traditional Furniture Factory:")
    client_code(TraditionalFurnitureFactory())