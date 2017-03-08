def AE():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def BCD(animal, sound):
    print("And on that farm he had a {}, Ee-igh, Ee-igh, Oh!".format(animal))
    #print("With a", sound "," sound, "here and a", sound ",", sound, "there.")
    print("With a {0}, {0} here and a {0}, {0} there.".format(sound))
    #print("Here a", sound ",", "there a", sound, "everywhere a", sound, sound ".")
    print("Here a {0}, there a {0}, everywhere a {0}, {0}.".format(sound))

def main():
    print("\n")
    AE()
    BCD("cow", "moo")
    AE()
    print("\n")
    AE()
    BCD("chicken", "cluck")
    AE()
    print("\n")
    AE()
    BCD("sheep", "baa")
    AE()
    print("\n")
    AE()
    BCD("goat", "neigh")
    AE()
    print("\n")
    AE()
    BCD("pig", "oink")
    AE()
    print("\n")

main()
