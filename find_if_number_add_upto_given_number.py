"""
problem: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""




def findIfTwoNumbersAddToGivenNumber(k,givenList):
    tmpNum = list(range(1,k+1,1))
    for i in range(len(tmpNum)):
        tempSet = set([tmpNum[i], tmpNum[len(tmpNum) - 1 - i]])
        if tempSet < set(givenList):
            return True
        else:
            pass
    
    return False



print(findIfTwoNumbersAddToGivenNumber(133, list(range(133))))
