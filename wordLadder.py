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

def isOneOff(wordOne, wordTwo):
    nodeOne = Node(wordOne, [])
    nodeTwo = Node(wordTwo, [])
    totalOff = 0
    for i in nodeOne.value:
        for j in nodeTwo.value:
            if i != j:
                totalOff +=1
                if totalOff > 1:
                    return False
    return True

#NOTES: review graph traversal problems and shortest path problems

class Graph:
    def __init__(self, beginNode, wordList):
        self.beginNode = beginNode
        self.wordList = wordList
        self.listNodes = []
        for word in wordList:
            wordNode = Node(word)
            if self.link(beginNode, wordNode)
                wordList.remove(wordNode.value)
            listNodes.append(beginNode)
        for word in wordList:
            wordNode = Node(word)
            i = 0
            while i<len(Nodes):
                nextNode(listNodes[i])
                if self.link(nextNode, wordNode)
                    wordList.remove(wordNode.value)
                i++

    def link(self, nodeOne, nodeTwo):
        if isOneOff(nodeOne.value, nodeTwo.value):
            nodeOne.neighbors.append(nodeTwo.value)
            return True
        return False


def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #create the graph
    if isOneOff()
