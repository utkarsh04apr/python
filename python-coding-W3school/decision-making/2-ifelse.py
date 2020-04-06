amount = int(input("enter amout:"))
print("money is =",amount)
if amount < 1000:
    discount = amount*.05
    print("discount is:",discount)
else:
    discount = amount*.1
    print("discount is:",discount)
print("total bill is:", amount - discount)

