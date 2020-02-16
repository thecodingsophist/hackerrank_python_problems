def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    #make hash
    wordlisthash = {}

    #get words from paragraph, store in hash
    for word in paragraph.split(" "):
        if word not in wordlisthash:
            wordlisthash[word.lower()] = 1
        else:
            wordlisthash[word.lower()] += 1

    #make unbanned wordlist
    #or, set word count of banned words to -1
    for word in banned.split(" "):
        print("banned word:", word)
        wordlisthash[word] = -1
    print("hash: ", wordlisthash)
    #take the greatest value
    maximum = max(wordlisthash.values())
    for word, count in wordlisthash.items():
        if count == maximum:
            return print(word)

if __name__ == "__main__":
    paragraph = "cat cat dog dog dog bark meow"
    banned = "meow"

    mostCommonWord(paragraph, banned)
