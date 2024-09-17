cost = float(input("How much did your meal cost?"))
tipprecent = input("How was your sevice bad, okay, good, or great\n")
if tipprecent == ("bad"):
    print(cost)
if tipprecent == ("okay"):
    print(cost*1.15)
if tipprecent == ("good"):
    print(cost*1.2)
if tipprecent == ("great"):
    print(cost*1.25)