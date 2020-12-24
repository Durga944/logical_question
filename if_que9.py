amount = 2400
transaction_type = "L"
if transaction_type == "L":
    if amount <= 25000:
        discount = amount*.0
        print( "Net Amount:", discount)
    if amount <=57000:
        discount = amount*.5
        print( "Net Amount:", discount)
else:
    if amount <=100000:
        discount = amount*.075
        print ("Net Amount:", discount)
    if amount >= 100000:
        discount = amount*.10
        print ("Net Amount:", discount )
