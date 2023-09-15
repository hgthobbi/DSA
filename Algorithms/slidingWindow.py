# sliding window is an algorithm that is an optimization on string/array problems that can be typically solved in O(n^2) or O(n^3)
# sliding window can bring the time complexity down to O(n)

# basic idea: we want to transform two nested for loops into a single loop
# in order to indentify a sliding window problem, consider: 
# 1. The problem will be based on a array or string that we will have to give the longest, shortest, or target values
# 2. The problem will ask us to find a subrange in that array or string
# The concept is mainly based on ideas like the longest sequence or shortest sequence of something that satisfies a given condition perfectly.

# init 2 pointers L, R in the beginning of the array

def slidingWindow(string):
    left, right = 0, len(string)
    hashDict = {}
    while right < len(string):
        if string[left] in hashDict:
            right+=1
        else:
            left+=1
        hashDict[string[left]] = string[left]
    return hashDict

print(slidingWindow('abcabcbb'))