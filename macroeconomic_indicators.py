# macroeconomic_indicators.py

class MacroeconomicIndicators:
    def __init__(self, gdp_current_year, gdp_last_year, cpi_current_year, cpi_last_year, labor_force, unemployed_people):
        self.gdp_current_year = gdp_current_year                # GDP of the current year
        self.gdp_last_year = gdp_last_year                      # GDP of the previous year
        self.cpi_current_year = cpi_current_year                # Consumer Price Index of the current year
        self.cpi_last_year = cpi_last_year                      # Consumer Price Index of the previous year
        self.labor_force = labor_force                          # Total labor force
        self.unemployed_people = unemployed_people              # Number of unemployed people

    def calculate_gdp_growth_rate(self):
        """Calculates the GDP growth rate as a percentage."""
        gdp_growth_rate = ((self.gdp_current_year - self.gdp_last_year) / self.gdp_last_year) * 100
        return gdp_growth_rate

    def calculate_inflation_rate(self):
        """Calculates the inflation rate based on CPI values."""
        inflation_rate = ((self.cpi_current_year - self.cpi_last_year) / self.cpi_last_year) * 100
        return inflation_rate

    def calculate_unemployment_rate(self):
        """Calculates the unemployment rate as a percentage."""
        unemployment_rate = (self.unemployed_people / self.labor_force) * 100
        return unemployment_rate

# Example usage:
gdp_last_year = 2.5e12          # GDP in dollars for the previous year
gdp_current_year = 2.7e12       # GDP in dollars for the current year
cpi_last_year = 250             # CPI of the previous year
cpi_current_year = 265          # CPI of the current year
labor_force = 160000000         # Total labor force
unemployed_people = 8000000     # Number of unemployed people

macro_indicators = MacroeconomicIndicators(gdp_current_year, gdp_last_year, cpi_current_year, cpi_last_year, labor_force, unemployed_people)

print(f"GDP Growth Rate: {macro_indicators.calculate_gdp_growth_rate():.2f}%")
print(f"Inflation Rate: {macro_indicators.calculate_inflation_rate():.2f}%")
print(f"Unemployment Rate: {macro_indicators.calculate_unemployment_rate():.2f}%")