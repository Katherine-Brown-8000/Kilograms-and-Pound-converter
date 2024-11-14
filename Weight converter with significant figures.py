metric = str(input("Enter K for Kilograms or L for pounds: "))
weight = float(input("Weight: "))


if metric == 'K':
    kc = weight*2.20
    print(f"The Weight in pounds is {kc:.2f}")
if metric == 'L':
    lc = weight/2.20
    print(f"The Weight in kilograms is {lc:.2f}")
