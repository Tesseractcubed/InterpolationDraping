import re
def inTomm(num_input):  # Consider using re and regex instead?
    num=""
    units=""
    for elem in num_input:
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
def fracToDecimal(num_input):
    pass
    # if input contains /, select numeric characters on either side;
    # Parse [0-9]+   [0-9]+/[0-9]+ as a number + fraction, and ignore the specific separators between them (accept -, &, and, etc.)
    # Specifically leave ## ##/## the first number alone
    # 
"""
# Test Program
def main ():
    num_in = input("Test")
    print(inTomm(num_in))

main()
"""