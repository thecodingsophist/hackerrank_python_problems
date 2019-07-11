def minion_game_solution1(string):
    # Problem: find the number of points scored by Stuart and Kevin by forming substring words from the string S starting with just vowels for Stuart and consonants for Kevin. Basically, how many substrings start with a vowel and how many start with a consonant?
    # Solution: Make a list of all substrings. Write a vowel_checker function to see if it starts with a vowel, if not, it must start with a consonant. Put it through the vowel_checker, award points to Stuart if it starts with a vowel. Award points to Kevin if not.

    # Make a list of all substrings
    # Brute force way: double for loop, make a list
    Kevin = 0 #count vowel substrings
    Stuart = 0
    substrings = []
    split_string = list(string)
    i = 0
    print("split_string:", split_string)
    for letter in split_string:
        for n in range(i+1, len(split_string)+1):
            print("substring: ", split_string[i:n])
            print("i:", i)
            print("n:", n)
            substrings += [''.join(split_string[i:n])]
        i += 1
    print("substrings", substrings)

    for item in substrings:
        if vowel_checker(item):
            Stuart += 1
        else:
            Kevin += 1

    print("Stuart", Stuart)
    print("Kevin", Kevin)
    if Stuart > Kevin:
        return print("Stuart", Stuart)
    elif Kevin > Stuart:
        return print("Kevin", Kevin)
    else:
         return print("Draw")

def vowel_checker(string):
    vowel = {"a":0, "e":0, "i":0, "o":0, "u":0}
    if string[0] in vowel:
        return True
    return False

def minion_game_solution2(string):
    # count the number of permutations is possible
    # add the number of vowel permutations together
    # compare the number of vowel permutations with (the number of permutations possible - the number of vowel permutations)

    # the number of permutations possible is:
    string_length = len(list(string))
    t_permutations = int(string_length*(string_length + 1)/2)
    # add together the number of vowel permutations
    v_permutations = 0
    i = 0
    while i < len(string):
        if vowel_checker(string[i]):
            v_permutations += len(string) - i
        i += 1

    # compare
    Kevin = v_permutations
    Stuart = t_permutations - v_permutations

    print("Stuart", Stuart)
    print("Kevin", Kevin)
    if Stuart > Kevin:
        return print("Stuart", Stuart)
    elif Kevin > Stuart:
        return print("Kevin", Kevin)
    else:
         return print("Draw")


if __name__ == '__main__':
    minion_game_solution2("banana")
