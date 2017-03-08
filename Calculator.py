def main():
    print("This app is designed to perform 100 requested calculations.")
    for i in range(100):
        ans = eval(input("Enter a requested a calculation: "))
        print(ans)
        i += 1
main()
