def inTomm(num_in):
    num=""
    units=""
    for elem in num_in:
        if elem.isnumeric() or elem ==".":
            num += elem
        else:
            units += elem

    match units:
        case "in":
            return 1
        case " in":
            return 1
        case _:
            global debug
            debug = 0
            if debug:
                print ("Unit mismatch error in unit conversion")
            print("Unit Conversion Error")
"""
# Test Program
def main ():
    num_in = input("Test")
    print(inTomm(num_in))

main()
"""