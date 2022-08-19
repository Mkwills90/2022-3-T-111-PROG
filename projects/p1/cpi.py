DECIMAL_DIGITS = 2

year_ago_cpi = float(input("Input CPI a year ago: ")) 
current_cpi = float(input("Input current CPI: "))
years_from_now = int(input("Input years: "))

absolute_change_cpi = current_cpi - year_ago_cpi
inflation = absolute_change_cpi / year_ago_cpi

print()
print("Change in CPI:", round(absolute_change_cpi, DECIMAL_DIGITS))
print("Inflation (%):", round(100 * inflation, DECIMAL_DIGITS))
print("CPI after", years_from_now, "years:", round(current_cpi * (1 + inflation) ** years_from_now, DECIMAL_DIGITS))