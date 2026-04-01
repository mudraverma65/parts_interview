# Task: Error Handling & Resilience
# Goal: Calculate a discount safely.

def calculate_discount(price, discount_percent):
    price_converted = int(price)
    discount_percent_int = int(discount_percent)

    if price <= 0 or discount_percent_int <=0:
        return 0

    return price / discount_percent_int 
    """
    Instructions: Handle cases where discount_percent is 0 
    or if inputs are strings/None. Return 0 for invalid inputs.
    """
    # TODO: Implement logic
    

# Test Case
print(calculate_discount(100, "10")) # Should return 0 or handle conversion
print(calculate_discount(100, 0))    # Should return 0