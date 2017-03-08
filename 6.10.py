def acronym(phrase):
    Sphrase = phrase.split()
    ac = ""
    for w in Sphrase:
        ac = ac + w[0]
    return ac

def main():
    phrase = input("Enter a phrase you want an acronym for: ")
    print("The acronym is {0}".format(acronym(phrase).upper()))
main()
