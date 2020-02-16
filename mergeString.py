def stripString(string):
    dict = {}
    for letter in string:
        if letter not in dict.keys():
            dict[letter] = 1
        else:
            dict[letter] += 1
    print(dict)
    return dict

def mergeStrings(s1, s2):
    a = len(s1)
    b = len(s2)
    a_strip = stripString(s1)
    b_strip = stripString(s2)
    mergedString = ""
    string = s1 + s2
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a_strip[s1[i]] > b_strip[s2[j]]:
            mergedString += s1[i]
            i += 1
        else if a_strip[s1[i]] < b_strip[s2[i]]:
            mergedString += s2[i]
            j += 1
        else:
            if s1[i] > s2[i]:
                mergedString += s1[i]
                i += 1
            else:
                mergedString += s2[i]
                j += 1

    return mergedString



if __name__ == '__main__':
