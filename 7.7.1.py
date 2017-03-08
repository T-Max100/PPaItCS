def babysitterBill(start, end):
    HS, MS = int(start[:2]), int(start[-2:])
    HE, ME = int(end[:2]), int(end[-2:])
    hours = HE - HS
    minutes = (ME - MS)/60
    Thours = hours + minutes
    m = int((Thours - Thours//1)*60)
    h = int(Thours//1)
    if HE > 21:
        Post21H = HE - 21
        Pre21H = Thours - Post21H
        bill = Post21H * 175 + Pre21H * 250
        bill_adj = (bill + 0.5)
        print("Your total time was {0}:{1}, or {0} hours and {1} minutes.".format(h,m))
        print("{} hours and {} minutes of the total time were after 9 (i.e. 21:00).".format(Post21H, ME))
        print("The bill is therefore ${:.2f}".format(bill_adj/100))
    else:
        bill = Thours * 250
        bill_adj = (bill + 0.5)//100
        print("Your total time was {0}:{1}, or {0} hours and {1} minutes".format(h,m))
        print("The bill is therefore ${:.2f}".format(bill_adj/100))

def main():
    print()
    print("This app uses a 24 hour clock to calculate a babysitter's bill.\n")
    start = input("Enter the start time (e.g. 24:00): ")
    end = input("Enter the end time (e.g. 24:00): ")
    print()
    babysitterBill(start, end)
    print()
main()
