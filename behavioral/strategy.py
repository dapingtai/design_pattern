from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, expiry: str):
        self._card_number = card_number
        self._expiry = expiry

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using Credit Card {self._card_number}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self._email = email

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount} using PayPal account {self._email}")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self._payment_strategy = payment_strategy
        self._amount = 0.0

    def set_payment_strategy(self, payment_strategy: PaymentStrategy) -> None:
        self._payment_strategy = payment_strategy

    def add_item(self, price: float) -> None:
        self._amount += price

    def checkout(self) -> None:
        self._payment_strategy.pay(self._amount)
        self._amount = 0.0

def main():
    # Create payment strategies
    credit_card = CreditCardPayment("1234-5678-9012-3456", "12/25")
    paypal = PayPalPayment("example@example.com")

    # Create shopping cart with credit card payment
    cart = ShoppingCart(credit_card)
    
    # Add items and checkout
    cart.add_item(100.0)
    cart.add_item(50.0)
    cart.checkout()

    # Change payment strategy to PayPal and checkout again
    cart.set_payment_strategy(paypal)
    cart.add_item(75.0)
    cart.checkout()

if __name__ == "__main__":
    main()