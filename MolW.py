print("This program determines the molecular weight of a hydrocarbon based on")
print("the number of hydrogen (H), carbon (C), and oxygen (O) atoms.")
print()
H, C, O = eval(input("Enter the number of hydrogens, carbons, and oxygens respectively, seperated by a comma: "))
W = H * 1.0079 + C * 12.011 + O * 15.9994
print("The total molecular weight is", W)
