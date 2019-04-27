#
# Complete the 'missingWords' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def missingWords(s, t):
    # Write your code here
    # missing_words_array = []
    j = 0
    marker_array = t.split(" ")
    word_array = s.split(" ")
    for word in marker_array:
        while j<len(word_array):
            if word == word_array[j]:
                word_array.remove(word)
                break
            else:
                j += 1
    return word_array

if __name__ == '__main__':
    print(str(missingWords("I like cheese like much", "like")) + " should return I and cheese and like and much")
    # print(str(missingWords("")))
