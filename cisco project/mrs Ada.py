print("welcome expenses tracker {-_-}")
amount=int(input("Enter the total amount of money taken to the market : "))
vat= 0.01
acc_balance=0
expense_list={}
def expense_tracker():
    expense_list={}
    no_items = int(input("what are the things you bought :   "))
    for i in range (no_items):
        items= input("Wha did tou buy ? ")
        cost_items=float(input ( " what is the cost "))
        expense_list.update({
            items:cost_items
        })
    for x in expense_list.values():
            total_exp=0
            total_exp +=x


    acc_balance = amount - total_exp * vat

    return acc_balance
    x=expense_tracker()
def compound_int():
    comp = expense_list() *( 1.05) **5

    print(comp)

print(expense_tracker())

