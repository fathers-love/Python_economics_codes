# Price Elasticity Calculation with Methods
class ElasticityCalculator:
    @staticmethod
    def price_elasticity(change_in_quantity, change_in_price, initial_quantity, initial_price):
        quantity_percentage_change = (change_in_quantity / initial_quantity) * 100
        price_percentage_change = (change_in_price / initial_price) * 100
        return quantity_percentage_change / price_percentage_change

elasticity = ElasticityCalculator.price_elasticity(10, -2, 50, 5)
print(f"Price Elasticity: {elasticity}")