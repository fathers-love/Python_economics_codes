# Calculating GDP Growth Rate
class GDPGrowthRateCalculator:
    def __init__(self, gdp_last_year, gdp_current_year):
        self.gdp_last_year = gdp_last_year
        self.gdp_current_year = gdp_current_year

    def growth_rate(self):
        return ((self.gdp_current_year - self.gdp_last_year) / self.gdp_last_year) * 100

# Example usage
gdp_calculator = GDPGrowthRateCalculator(2.5e12, 2.7e12)  # in dollars
print(f"GDP Growth Rate: {gdp_calculator.growth_rate():.2f}%")