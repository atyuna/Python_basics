def my_adder(a, b):
    total = a + b
    return total


my_total = my_adder(3, 6)
print(my_total)


# Example: function to find if the state has no sales tax:

def has_no_sales_tax(state):
    states_with_no_sale_tax = ["AK", "DE", "MT", "NH", "OR"]
    if state.upper() in states_with_no_sale_tax:
        return True
    else:
        return False


user_state = "NC"
tax = has_no_sales_tax(user_state)
print(tax)
