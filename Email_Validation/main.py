# Email Validation using string function

email = input("Enetr your Email-Id: ")
k = 0
if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):  # '^' => XOR Operator
                for x in email:
                    if x == x.isspace():
                        k = 1
                    elif x.isalpha():
                        if x == x.upper():
                            k = 2
                    elif x.isdigit():
                        continue
                    elif x == "_" or x == "." or x == "@":
                        continue
                    else:
                        k = 3
                if k == 1 or k == 2 or k == 3:
                    print("wrong Email #5")
                else:
                    print("Valid Email")
            else:
                print("wrong Email #4")
        else:
            print("wrong Email #3")
    else:
        print("wrong Email #2")
else:
    print("Wrong Email #1")
