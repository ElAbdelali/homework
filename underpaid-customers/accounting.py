melon_cost = 1.00
def customer_expected(filename):
    for line in open(filename):
        line = line.rstrip()
        word = line.split('|')
        
        customer_num = word[0]
        customer_name = word[1]
        melon_amount = float(word[2])
        amount_paid = float(word[3])
        
        amount_owed = melon_amount * melon_cost
        
        if amount_owed == amount_paid:
            print(f"Customer {customer_num}, {customer_name} paid ${amount_paid:.2f}, they did not overpay/underpay.")
        elif amount_owed > amount_paid:
            difference = amount_owed - amount_paid
            print(f"Customer {customer_num}, {customer_name} paid ${amount_paid:.2f}, they owed {amount_owed:.2f}. They underpaid by ${difference:.2f}.")
        elif amount_owed < amount_paid:
            difference = amount_paid - amount_owed
            print(f"Customer {customer_num}, {customer_name} paid ${amount_paid:.2f}, they owed {amount_owed:.2f}. They overpaid by ${difference:.2f}.")
        

customer_expected("customer-orders.txt")