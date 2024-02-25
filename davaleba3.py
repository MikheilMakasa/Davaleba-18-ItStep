def commission_decorator(func):
    def wrapper(balance, amount):
        commission = 1  
        if balance >= amount + commission:
            result = func(balance, amount)
            print(f"Transaction successful, deducted {commission} GEL in commission.")
            return result
        else:
            raise ValueError("Insufficient balance for the transaction.")
    return wrapper

@commission_decorator
def perform_transaction(balance, amount):
    new_balance = balance - amount
    return new_balance


try:
    balance = 100
    amount_to_pay = 99
    perform_transaction(balance, amount_to_pay)
    

    balance = 100
    amount_to_pay = 110
    perform_transaction(balance, amount_to_pay) 
except ValueError as e:
    print(f"Error: {e}")
