from enum import Enum
from functools import total_ordering

import pandas as pd

class Book:
    """An instrument book"""

    def __init__(self, name):
        self.name = name
        self.buy = []
        self.sell = []
        self.counter = 0

    def insert_buy(self, quantity, price):
        self.insert(self.buy, Order(quantity, price, Side.BUY))

    def insert_sell(self, quantity, price):
        self.insert(self.sell, Order(quantity, price, Side.SELL))
    
    def insert(self, side_orders, order):
        """
        Insert an order in this side, keeping it ordered from best to worst.
        For instance the best buy (resp. sell) order is the one with the highest (resp. lowest) price.
        """
        self.counter += 1
        order.counter = self.counter
        side_orders.append(order)
        side_orders.sort() # rely on natural object ordering
        print('Insert %s on %s' % (order, self.name))

        self.check_execs()
        print(repr(self))
    
    def _can_execute(self):
        return self.buy and self.sell and (self.buy[0].price >= self.sell[0].price)

    def check_execs(self):
        """Check if best orders on each side can be executed."""
        while self._can_execute():
            buy = self.buy[0]
            sell = self.sell[0]
            execQty = min(buy.quantity, sell.quantity)
            execPrice = buy.price if buy.counter < sell.counter else sell.price

            print('Execute %s at %s on %s' % (execQty, execPrice, self.name))

            if (buy.quantity <= execQty): del self.buy[0]
            else: buy.quantity = buy.quantity - execQty
            
            if (sell.quantity <= execQty): del self.sell[0]
            else: sell.quantity = sell.quantity - execQty
    
    def __repr__(self):
        def print_side(orders, side):
            if orders:
                return str(pd.DataFrame([o.__dict__ for o in orders]))
            else:
                return "No %s orders" % side.name

        return '''
--------
%s
%s
%s
--------''' % (
            self.name,
            print_side(self.buy, Side.BUY),
            print_side(self.sell, Side.SELL))



class Side(Enum):
    BUY = 1
    SELL = 2


@total_ordering
class Order:
    """A trader order"""

    def __init__(self, quantity, price, side, counter=None):
        self.quantity = quantity
        self.price = price
        self.side = side
        self.counter = counter

    def _is_valid_operand(self, other):
        return (hasattr(other, "side") and
                hasattr(other, "price") and
                hasattr(other, "counter"))
    
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.side, self.price, self.counter) == (other.side, other.price, other.counter)

    def __lt__(self, other):
        """Order best order (lowest sell or highest buy) first, for same price use insertion order."""
        if not self._is_valid_operand(other):
            return NotImplemented
        if self.side != other.side:
            return NotImplemented
        if self.price == other.price: return self.counter < other.counter
        elif self.side == Side.BUY: return self.price > other.price
        elif self.side == Side.SELL: return self.price < other.price
    
    def __repr__(self):
        return '%s %s@%s id=%s' % (self.side.name, self.quantity, self.price, self.counter)

