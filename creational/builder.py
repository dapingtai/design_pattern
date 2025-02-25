"""
Builder Pattern Implementation

建造者模式使用多個簡單的對象一步一步構建成一個複雜的對象。
這個例子展示了如何使用建造者模式來構建一個複雜的電腦對象。
"""

from abc import ABC, abstractmethod

# Product
class Computer:
    def __init__(self):
        self.parts = {}
    
    def add_part(self, key: str, value: str):
        self.parts[key] = value
    
    def show(self):
        print("Computer parts:")
        for key, value in self.parts.items():
            print(f"{key}: {value}")

# Abstract Builder
class ComputerBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def build_cpu(self):
        pass
    
    @abstractmethod
    def build_memory(self):
        pass
    
    @abstractmethod
    def build_storage(self):
        pass
    
    @abstractmethod
    def get_result(self) -> Computer:
        pass

# Concrete Builder
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._computer = Computer()
    
    def build_cpu(self):
        self._computer.add_part("CPU", "High-end Gaming CPU")
    
    def build_memory(self):
        self._computer.add_part("Memory", "32GB Gaming RAM")
    
    def build_storage(self):
        self._computer.add_part("Storage", "2TB NVMe SSD")
    
    def get_result(self) -> Computer:
        computer = self._computer
        self.reset()
        return computer

class OfficeComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._computer = Computer()
    
    def build_cpu(self):
        self._computer.add_part("CPU", "Standard Office CPU")
    
    def build_memory(self):
        self._computer.add_part("Memory", "8GB RAM")
    
    def build_storage(self):
        self._computer.add_part("Storage", "256GB SSD")
    
    def get_result(self) -> Computer:
        computer = self._computer
        self.reset()
        return computer

# Director
class ComputerAssembler:
    def __init__(self):
        self._builder = None
    
    def set_builder(self, builder: ComputerBuilder):
        self._builder = builder
    
    def construct_computer(self):
        self._builder.build_cpu()
        self._builder.build_memory()
        self._builder.build_storage()

# Client Code
if __name__ == "__main__":
    assembler = ComputerAssembler()
    gaming_builder = GamingComputerBuilder()
    office_builder = OfficeComputerBuilder()
    
    print("Building a gaming computer:")
    assembler.set_builder(gaming_builder)
    assembler.construct_computer()
    gaming_computer = gaming_builder.get_result()
    gaming_computer.show()
    
    print("\nBuilding an office computer:")
    assembler.set_builder(office_builder)
    assembler.construct_computer()
    office_computer = office_builder.get_result()
    office_computer.show()