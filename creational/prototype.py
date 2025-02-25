"""
Prototype Pattern Implementation

原型模式通過複製現有對象來創建新對象，而不是通過實例化的方式。
這個例子展示了如何使用原型模式來複製不同類型的文檔。
"""

import copy
from abc import ABC, abstractmethod

class DocumentPrototype(ABC):
    def __init__(self):
        self.type = None
        self.content = None
    
    @abstractmethod
    def clone(self):
        pass

class TextDocument(DocumentPrototype):
    def __init__(self):
        super().__init__()
        self.type = "Text"
        self.content = ""
        self.font_size = 12
        self.font_name = "Arial"
    
    def set_content(self, content: str):
        self.content = content
    
    def set_font(self, name: str, size: int):
        self.font_name = name
        self.font_size = size
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Type: {self.type}\nContent: {self.content}\nFont: {self.font_name}, Size: {self.font_size}"

class SpreadsheetDocument(DocumentPrototype):
    def __init__(self):
        super().__init__()
        self.type = "Spreadsheet"
        self.content = {}
        self.rows = 0
        self.columns = 0
    
    def set_dimensions(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
    
    def set_cell_content(self, row: int, column: int, content: str):
        self.content[(row, column)] = content
    
    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        result = f"Type: {self.type}\nDimensions: {self.rows}x{self.columns}\nContent:\n"
        for (row, col), content in self.content.items():
            result += f"Cell({row},{col}): {content}\n"
        return result

# Client Code
if __name__ == "__main__":
    # Create and setup original text document
    original_text = TextDocument()
    original_text.set_content("Hello World")
    original_text.set_font("Times New Roman", 14)
    
    # Clone text document
    cloned_text = original_text.clone()
    cloned_text.set_content("Modified Hello World")
    
    print("Original Text Document:")
    print(original_text)
    print("\nCloned Text Document:")
    print(cloned_text)
    
    # Create and setup original spreadsheet
    original_sheet = SpreadsheetDocument()
    original_sheet.set_dimensions(2, 2)
    original_sheet.set_cell_content(0, 0, "A1")
    original_sheet.set_cell_content(0, 1, "B1")
    
    # Clone spreadsheet
    cloned_sheet = original_sheet.clone()
    cloned_sheet.set_cell_content(1, 0, "A2")
    cloned_sheet.set_cell_content(1, 1, "B2")
    
    print("\nOriginal Spreadsheet:")
    print(original_sheet)
    print("\nCloned Spreadsheet:")
    print(cloned_sheet)