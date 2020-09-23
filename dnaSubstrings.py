# dnaSubstrings.py
# Marcela Gomez

# This program searches for the string t in string s and ourputs
# the indexes of each starting position and the number of times it occurs.

def getStrings():
    infile = open("motifFinding.txt","r")
    dnaFinder = infile.readlines()
    S = dnaFinder[0].rstrip()
    T = dnaFinder[1].rstrip()
    return S, T

def main():

    s,t = getStrings()
    indexList = []

    for i in range(len(s)):
        if t == s[i:i+len(t)]:
            indexList.append(i)

    print("The sub string t is found in s at the following index positions:")
    for i in range(len(indexList)-1):
        print(indexList[i],sep=",", end=", ")
    print(indexList[-1],end=".")
    
main()

    
