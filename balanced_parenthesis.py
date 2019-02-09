# This is the classic open parenthesis, closed parenthesis question
# Parenthesis must be balanced, return True or False is balanced or not

def balanced_parenthesis(string):
    #clean input to just parenthesis
    clean_input = ""
    for input in string:
        if input == "(" or input == ")":
            clean_input += input
    #now evaluate the balancedness of parenthesis
    if len(clean_input)%2 != 0:
        print("F")
        return False
    return balanced(clean_input)


def balanced(string):
    #check for "units"
    open = []
    # so_far = ""
    for input in string:
        # so_far += input
        if input == "(":
            open += ["("]
        elif input == ")" and len(open) > 0:
            open.pop()
        else:
            print("F")
            return False
    if open == []:
        print("T")
        return True

    print("F")
    return False






#RUN FUNCTION
string0 = "(" #return False
string1 = "()" #return True
#basically the string has to be even
string2 = "((()))" #return True
string3 = "(()(" #return False
#the number of open parenthesis has to equal the number of closed parenthesis
string4 = "))((" #return False
balanced_parenthesis(string4)
