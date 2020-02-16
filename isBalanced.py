def isBalancedTryOne(string):
    l = len(string)
    if l%2 != 0:
        return "NO"
    else:
        first_half_len = int(l/2)
        print("first_half_len=" + str(first_half_len))
        second_half = string[first_half_len:]
        print("second_half=" + str(second_half))
        second_half_reversed = second_half[len(second_half)::-1]
        print("second_half_reversed: " + second_half_reversed)
        first_half = string[:first_half_len]
        print("first_half: " + first_half)
        second_half_reversed_runthrough = ""
        for i in second_half_reversed:
            if i == ")":
                second_half_reversed_runthrough += "("
            elif i == "]":
                second_half_reversed_runthrough += "["
            elif i == "}":
                second_half_reversed_runthrough += "{"
        print("second_half_reversed_runthrough" + second_half_reversed_runthrough)
        if first_half == second_half_reversed_runthrough:
            return "YES"
        else:
            return "NO"

def check(stringA, stringB):
    if  stringA == ')' and stringB == '(':
        return True
    elif stringA == ']' and stringB == '[':
        return True
    elif stringA == '}' and stringB == '{':
        return True
    return False

def isBalanced(string):
    stack = []
    for i in string:
        # print("i: " + i)
        if i == "[" or i == "{" or i == "(":
            stack.append(i)
            # print("stack begin: " + str(stack))
        else:
            # print("i check: " + i)
            # print("stack check: " + stack[-1])
            if len(stack) == 0:
                return "NO"
            elif check(i, stack[-1]):
                stack.pop()
                # print(stack)
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    print(isBalanced("()")) #YES
    print(isBalanced("[]]")) #NO
    print(isBalanced("((({{[]}})))")) #YES
    print(isBalanced("()[]{}")) #YES
