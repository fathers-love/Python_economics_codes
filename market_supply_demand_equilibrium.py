# Market Equilibrium: Supply and Demand with Calculations
class Market:
    def __init__(self, supply_func, demand_func):
        self.supply_func = supply_func
        self.demand_func = demand_func

    def equilibrium_price(self):
        for price in range(1, 100):
            if self.supply_func(price) == self.demand_func(price):
                return price
        return None

# Supply and demand functions
supply = lambda p: 2 * p
demand = lambda p: 100 - 3 * p

market = Market(supply, demand)
print(f"Equilibrium price: {market.equilibrium_price()}")