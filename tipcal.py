cost = float(input("How much did your meal cost?"))
tipprecent = input("How was your sevice bad, okay, good, or great\n")
if tipprecent == ("bad"):
    print(("Your total is ") + str(cost))
elif tipprecent == ("okay"):
    print(("Your total is ") + str(cost*1.15))
elif tipprecent == ("good"):
    print(("Your total is ") + str(cost*1.2))
elif tipprecent == ("great"):
    print(("Your total is ") + str(cost*1.25))