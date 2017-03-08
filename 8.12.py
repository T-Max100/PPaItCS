# text source here: http://academic.udayton.edu/kissock/http/Weather/gsod95-current/NYNEWYOR.txt
# trick to figuring out how to delete the right number of characters from the text file here: http://superuser.com/questions/339601/how-would-i-delete-the-first-27-characters-from-every-line-notepad

def calc(T, f):
    line = f.readline()
    d = 1
    l = [0, 0]
    while T != '':
        #print("T is", T)
        T = float(T)
        if T < 60:
            l[0] += 60 - T
        elif T > 80:
            l[1] += T - 80
        line = f.readline()
        T = line
        d += 1
    print("\nIn {} days, there were {:.0f} heating degree days and {:.0f} cooling degree days.\n".format(d, l[0], l[1]))

def main():
    print("\nThis app computes the number of cooling and heating days.")
    fileName = input("What file are the entries in? ")
    infile = open(fileName, 'r')
    line = infile.readline()
    T = line
    calc(T, infile)
main()
