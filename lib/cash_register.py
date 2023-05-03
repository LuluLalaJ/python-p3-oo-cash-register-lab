#!/usr/bin/env python3

class CashRegister:

    def __init__(self, discount=0) -> None:
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = []

    def add_item(self, title, price, quantity=1):
        self.total += price*quantity
        self.last_transaction = [title, price, quantity]
        # use _ when we don't really care what is being iterated
        # we only care that we go through a certain times
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount:
            self.total *= (100-self.discount)/100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")


    def void_last_transaction(self):
        self.total -= self.last_transaction[1]*self.last_transaction[2]
        for _ in range(self.last_transaction[2]):
            self.items.pop()
