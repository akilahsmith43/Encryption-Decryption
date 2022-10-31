
print("Start of Calculator Program")
# Assignment #2

no_adds = 0
no_subs = 0
no_multi = 0
no_exponent = 0
no_divs = 0
no_modulus = 0
no_floor_divs =0

log_string = " "




while True:
    op = input("Please use one of these arithmetic operators: +, -, *, /, **, %, // \n")
    a = int(input("Enter the input number: "))
    b = int(input("Enter the second number: "))
    while op not in '+, -, *, /, **, %, //':
        op = input("error, re-enter \n")
    if op == "+":
        log_string += str(a) + ' + ' + str(b)+ '= ' + str(a + b) + "\n"
        no_adds += 1
        print(a + b)
    elif op == "-":
        log_string = str(a) + '- ' + str(b) + '= ' + str(a - b)
        no_subs += 1
        print(a - b)
    elif op == "*":
        log_string = str(a) + '* ' + str(b) + '= ' + str(a * b)
        no_multi += 1
        print(a * b)
    elif op == "/":
        log_string = str(a) + '/ ' + str(b) + '= ' + str(a / b)
        no_divs += 1
        print(a / b)
    elif op == "//":
        log_string = str(a) + '// ' + str(b) + '= ' + str(a // b)
        no_floor_divs += 1
        print(a // b)
    elif op == "**":
        log_string = str(a) + '** ' + str(b) + '= ' + str(a ** b)
        no_exponent += 1
        print(a ** b)
    elif op == "%":
        log_string = str(a) + '% ' + str(b) + '= ' + str(a % b)
        no_modulus += 1
        print(a % b)
    else:
        print("Error")
        exit()

    more = input("Do you have more calculations (“y” or “n”) ? \n")
    if more not in "yesYesYES":
        print("Number of times + was used:" , no_adds)
        print("Number of times - was used:" ,no_subs)
        print("Number of times * was used:" ,no_multi)
        print("Number of times ** was used:" ,no_exponent)
        print("Number of times / was used:" ,no_divs)
        print("Number of times % was used:" ,no_modulus)
        print("Number of times // was used:" ,no_floor_divs)
        break
input ("\n\nHit Enter to end program")









