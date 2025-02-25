from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer) -> None:
        """Attach an observer to the subject."""
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        """Detach an observer from the subject."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notify all observers about an event."""
        pass

class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state changes.
    """

    _state: int = None
    _observers: List = []

    def attach(self, observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """Trigger an update in each subscriber."""
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self._state)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        print("\nSubject: I'm doing something important.")
        self._state = round(0.5)
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, state: int) -> None:
        """Receive update from subject."""
        pass

class ConcreteObserverA(Observer):
    def update(self, state: int) -> None:
        print(f"ConcreteObserverA: Reacted to the state change: {state}")

class ConcreteObserverB(Observer):
    def update(self, state: int) -> None:
        print(f"ConcreteObserverB: Reacted to the state change: {state}")

def main():
    # The client code
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)
    subject.some_business_logic()

if __name__ == "__main__":
    main()