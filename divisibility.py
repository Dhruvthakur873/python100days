# num = float(input("Enter a number: "))
for num in range(0,101):
    if num%3==0 and num%5==0:
        if num%15!=0:
            print("wow! we got it ")
        else:
            print("divisible by 3 and 5 but also by 15")
    else: 
        print("not divisible by 3 and 5 and 15")