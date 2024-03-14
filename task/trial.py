def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# Example usage:
base_value = 10
exponent_value = 3
result = large_power(base_value, exponent_value)
print(f"Is {base_value} raised to the power of {exponent_value} greater than 5000? {result}")


# /
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

# Example usage:
number_to_check = 30
result = divisible_by_ten(number_to_check)
print(f"Is {number_to_check} divisible by ten? {result}")
