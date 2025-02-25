from abc import ABC, abstractmethod
from typing import Dict

# Mediator Interface
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, msg: str, user) -> None:
        pass

    @abstractmethod
    def add_user(self, user) -> None:
        pass

# Concrete Mediator
class ChatRoom(ChatMediator):
    def __init__(self):
        self._users: Dict = {}  # Dictionary of users

    def add_user(self, user) -> None:
        self._users[user.name] = user

    def send_message(self, msg: str, user) -> None:
        # Send message to all users except the sender
        for name, u in self._users.items():
            if u != user:
                u.receive(msg)

# User Interface
class User:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self._mediator = mediator
        self._mediator.add_user(self)

    def send(self, msg: str) -> None:
        print(f"{self.name} sending message: {msg}")
        self._mediator.send_message(msg, self)

    def receive(self, msg: str) -> None:
        print(f"{self.name} received message: {msg}")

def main():
    # Create mediator
    chat_room = ChatRoom()

    # Create users
    alice = User("Alice", chat_room)
    bob = User("Bob", chat_room)
    charlie = User("Charlie", chat_room)

    # Send some messages
    alice.send("Hello everyone!")
    bob.send("Hi Alice!")
    charlie.send("Hi guys!")

if __name__ == "__main__":
    main()