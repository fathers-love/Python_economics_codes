# Calculating Inflation Rate based on Consumer Price Index (CPI)
class InflationCalculator:
    def __init__(self, cpi_last_year, cpi_current_year):
        self.cpi_last_year = cpi_last_year
        self.cpi_current_year = cpi_current_year

    def inflation_rate(self):
        return ((self.cpi_current_year - self.cpi_last_year) / self.cpi_last_year) * 100

# Example usage
calculator = InflationCalculator(250, 275)
print(f"Inflation Rate: {calculator.inflation_rate():.2f}%")