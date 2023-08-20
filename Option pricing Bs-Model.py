import math

def calculate_black_scholes(option_type, spot_price, strike_price, interest_rate, volatility, time_to_maturity_days):
    time_to_maturity_years = time_to_maturity_days / 365.0
    
    d1 = (math.log(spot_price / strike_price) + (interest_rate + 0.5 * volatility**2) * time_to_maturity_years) / (volatility * math.sqrt(time_to_maturity_years))
    d2 = d1 - volatility * math.sqrt(time_to_maturity_years)
    
    if option_type == "call":
        option_price = spot_price * norm.cdf(d1) - strike_price * math.exp(-interest_rate * time_to_maturity_years) * norm.cdf(d2)
    elif option_type == "put":
        option_price = strike_price * math.exp(-interest_rate * time_to_maturity_years) * norm.cdf(-d2) - spot_price * norm.cdf(-d1)
    else:
        option_price = None
    
    return option_price

from scipy.stats import norm

option_type = input("Enter option type (call/put): ")
spot_price = float(input("Enter spot price: "))
strike_price = float(input("Enter strike price: "))
interest_rate = float(input("Enter interest rate: ")) / 100.0
volatility = float(input("Enter volatility: ")) / 100.0
time_to_maturity_days = float(input("Enter time to maturity (in days): "))

option_price = calculate_black_scholes(option_type, spot_price, strike_price, interest_rate, volatility, time_to_maturity_days)
print(f"Option Price: {option_price}")
