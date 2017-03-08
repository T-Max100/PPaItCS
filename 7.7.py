def babysitterBill(start, end):
    HS, MS = int(start[:2]), int(start[-2:])
    HE, ME = int(end[:2]), int(end[-2:])
    hours = HE - HS
    minutes = (ME - MS)/60
    print("minutes", minutes)
    Thours = hours + minutes
    m = int((Thours - Thours//1)*60)
    print("m", m)
    h = int(Thours//1)
    print("h", h)
    if HE > 21:
        print(HE)
        Post21H = HE - 21
        print(Post21H)
        Pre21H = Thours - Post21H
        print(Pre21H)
        bill = Post21H * 1.75 + Pre21H * 2.50
        print(bill)
        print("Your total time was {0}:{1}, or {0} hours and {1} minutes.".format(h,m))
        print("{} hours and {} minutes of the total time were after 9 (i.e. 21:00).".format(Post21H, ME))
        print("The bill is therfore ${:.2f}".format(bill))
    else:
        bill = Thours * 2.50
        print("Your total time was {0}:{1}, or {0} hours and {1} minutes".format(h,m))
        print("The bill is therfore ${:.2f}".format(bill))

def main():
    print()
    print("This app uses a 24 hour clock to calculate a babysitter's bill.\n")
    start = input("Enter the start time (e.g. 24:00): ")
    end = input("Enter the end time (e.g. 24:00): ")
    babysitterBill(start, end)
    print()
main()
