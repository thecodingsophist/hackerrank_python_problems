# def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#     return
#
# def nextRung(beginWord, endWord, wordList):
#     diffList = []
#     oneOffList = []
#     newWord = ""
#     for word in wordList:
#         if isOneOff(beginWord, word):
#             oneOffList.append(word)
#     for compare in wordList:
#         for word in OneOffList:
#             diffList.append(isHowManyOff(word, compare))
#
#     return newWord
#
# def isHowManyOff(wordOne, wordTwo):
#     totalOff = 0
#     for i in wordOne:
#         for j in wordTwo:
#             if i != j:
#                 totalOff +=1
#     return totalOff
#

class Node:
    def __init__(self, value, neighbors):
        self.value = value
        self.neighbors = neighbors

def isOneOff(rungOne, rungTwo):
    totalOff = 0
    for i in rungOne.node:
        for j in rungTwo.node:
            if i != j:
                totalOff +=1
                if totalOff > 1:
                    return False
    return True

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #create the graph
    if isOneOff()
