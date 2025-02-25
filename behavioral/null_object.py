from abc import ABC, abstractmethod

# Abstract Logger
class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

    @abstractmethod
    def warn(self, message: str) -> None:
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        pass

# Concrete Logger
class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"LOG: {message}")

    def warn(self, message: str) -> None:
        print(f"WARNING: {message}")

    def error(self, message: str) -> None:
        print(f"ERROR: {message}")

# Null Object Logger
class NullLogger(Logger):
    def log(self, message: str) -> None:
        pass  # Do nothing

    def warn(self, message: str) -> None:
        pass  # Do nothing

    def error(self, message: str) -> None:
        pass  # Do nothing

# Service using the logger
class UserService:
    def __init__(self, logger: Logger = NullLogger()):
        self._logger = logger

    def create_user(self, name: str) -> None:
        # Attempt to create user
        try:
            # Simulate user creation
            print(f"Creating user: {name}")
            self._logger.log(f"User '{name}' created successfully")
        except Exception as e:
            self._logger.error(f"Failed to create user '{name}': {str(e)}")

def main():
    # Using concrete logger
    console_logger = ConsoleLogger()
    service_with_logging = UserService(console_logger)
    service_with_logging.create_user("Alice")

    print("\n" + "="*50 + "\n")

    # Using null logger
    service_without_logging = UserService()  # Uses NullLogger by default
    service_without_logging.create_user("Bob")

if __name__ == "__main__":
    main()