"""
Singleton Pattern Implementation

單例模式確保一個類只有一個實例，並提供一個存取該實例的全局存取點。
這個例子展示了如何使用單例模式來實現一個配置管理器。
"""

class ConfigurationManager:
    # Private class instance variable
    _instance = None
    
    def __new__(cls):
        # Create object if it's not already created
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            # Initialize the singleton instance
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Initialize the singleton instance (called only once)"""
        self._config = {}
    
    def set_config(self, key: str, value: str):
        """Set a configuration value"""
        self._config[key] = value
    
    def get_config(self, key: str) -> str:
        """Get a configuration value"""
        return self._config.get(key)
    
    def list_configs(self) -> dict:
        """Get all configurations"""
        return self._config.copy()

# Alternative Implementation using a Decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        self.log_records = []
    
    def log(self, message: str):
        self.log_records.append(message)
        print(f"Logged: {message}")
    
    def get_logs(self):
        return self.log_records.copy()

# Client Code
if __name__ == "__main__":
    # Testing ConfigurationManager Singleton
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    
    print("Testing ConfigurationManager Singleton:")
    print(f"Are config1 and config2 the same instance? {config1 is config2}")
    
    config1.set_config("database", "mongodb://localhost:27017")
    config1.set_config("api_key", "secret123")
    
    print("\nConfigurations set through config1:")
    print(config1.list_configs())
    
    print("\nAccessing configurations through config2:")
    print(config2.list_configs())
    
    # Testing Logger Singleton (decorator implementation)
    print("\nTesting Logger Singleton:")
    logger1 = Logger()
    logger2 = Logger()
    
    print(f"Are logger1 and logger2 the same instance? {logger1 is logger2}")
    
    logger1.log("First log message")
    logger2.log("Second log message")
    
    print("\nAll logs (accessed through logger1):")
    print(logger1.get_logs())
    
    print("\nAll logs (accessed through logger2):")
    print(logger2.get_logs())