amount = int(input("enter amount:"))
if amount<1000:
    discount=amount*.05
    print("discount is:",discount)
elif amount<5000:
    discount=amount*.1
    print("discount is:",discount)
elif amount<10000:
    discount=amount*.15
    print("discount is:",discount)
else:
    discount=amount*.2
    print("discount is:",discount)
print("bill is:",amount-discount)


