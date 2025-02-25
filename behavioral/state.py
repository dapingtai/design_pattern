from abc import ABC, abstractmethod

# State Interface
class State(ABC):
    @abstractmethod
    def handle(self) -> None:
        pass

    @abstractmethod
    def switch(self, context) -> None:
        pass

# Concrete States
class WorkingState(State):
    def handle(self) -> None:
        print("Traffic Light: Green - Cars can go")

    def switch(self, context) -> None:
        context.state = WaitingState()

class WaitingState(State):
    def handle(self) -> None:
        print("Traffic Light: Yellow - Cars should slow down")

    def switch(self, context) -> None:
        context.state = StoppingState()

class StoppingState(State):
    def handle(self) -> None:
        print("Traffic Light: Red - Cars must stop")

    def switch(self, context) -> None:
        context.state = WorkingState()

# Context
class TrafficLight:
    def __init__(self):
        self._state = WorkingState()

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, state: State) -> None:
        self._state = state

    def change(self) -> None:
        self._state.handle()
        self._state.switch(self)

def main():
    # Create traffic light
    traffic_light = TrafficLight()

    # Change states
    for _ in range(6):
        traffic_light.change()

if __name__ == "__main__":
    main()