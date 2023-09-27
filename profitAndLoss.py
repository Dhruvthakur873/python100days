s_price = float(input("Enter the selling price: "))
cost_price = float(input("Enter the cost price: "))
if cost_price>s_price:
    loss = cost_price - s_price
    print("has incurred loss of: ",loss)
else :
    profit = s_price - cost_price
    print("has incurred  profit of: ", profit)   