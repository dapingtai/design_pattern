from __future__ import annotations
from typing import List
import datetime

# Memento
class EditorMemento:
    def __init__(self, content: str) -> None:
        self._content = content
        self._date = datetime.datetime.now()

    @property
    def content(self) -> str:
        return self._content

    @property
    def date(self) -> datetime.datetime:
        return self._date

# Originator
class Editor:
    def __init__(self) -> None:
        self._content = ""

    def type(self, words: str) -> None:
        self._content += words

    def get_content(self) -> str:
        return self._content

    def save(self) -> EditorMemento:
        return EditorMemento(self._content)

    def restore(self, memento: EditorMemento) -> None:
        self._content = memento.content

# Caretaker
class History:
    def __init__(self) -> None:
        self._mementos: List[EditorMemento] = []

    def push(self, memento: EditorMemento) -> None:
        self._mementos.append(memento)

    def pop(self) -> EditorMemento:
        return self._mementos.pop()

def main():
    editor = Editor()
    history = History()

    # First change
    editor.type("First line of text. ")
    history.push(editor.save())

    # Second change
    editor.type("Second line of text. ")
    history.push(editor.save())

    # Third change
    editor.type("Third line of text.")
    print(f"Current content: {editor.get_content()}")

    # Undo last change
    editor.restore(history.pop())
    print(f"First undo: {editor.get_content()}")

    # Undo one more change
    editor.restore(history.pop())
    print(f"Second undo: {editor.get_content()}")

if __name__ == "__main__":
    main()