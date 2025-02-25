from abc import ABC, abstractmethod
from typing import Optional

# Handler Interface
class Handler(ABC):
    def __init__(self) -> None:
        self._next_handler: Optional[Handler] = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> str:
        pass

# Concrete Handlers
class DirectorHandler(Handler):
    def handle(self, request: str) -> str:
        if request == "Vacation":
            return f"Director: I'll handle the {request} request."
        elif self._next_handler:
            return self._next_handler.handle(request)
        return f"No one can handle the {request} request."

class ManagerHandler(Handler):
    def handle(self, request: str) -> str:
        if request == "Purchase":
            return f"Manager: I'll handle the {request} request."
        elif self._next_handler:
            return self._next_handler.handle(request)
        return f"No one can handle the {request} request."

class TeamLeadHandler(Handler):
    def handle(self, request: str) -> str:
        if request == "Leave":
            return f"Team Lead: I'll handle the {request} request."
        elif self._next_handler:
            return self._next_handler.handle(request)
        return f"No one can handle the {request} request."

def main():
    # Create handlers
    director = DirectorHandler()
    manager = ManagerHandler()
    team_lead = TeamLeadHandler()

    # Set up chain
    team_lead.set_next(manager).set_next(director)

    # Send requests
    print(team_lead.handle("Leave"))      # Handled by Team Lead
    print(team_lead.handle("Purchase"))   # Handled by Manager
    print(team_lead.handle("Vacation"))   # Handled by Director
    print(team_lead.handle("Coffee"))     # Not handled

if __name__ == "__main__":
    main()