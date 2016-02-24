# Write a method/function/code fragment in a high level language (Java, C++, etc) which
# prints all permutations of {1, 2, 3, . . . , n}.

#Python has a permutation function already defined:
#from itertools import permutations
#for i in permutations(n2,len(n2)):
#    print(i)

#Following is recursive and my implementation:
import operator

def permuterDriver(n):
    #Store n as a list
    n2 = [y for y in range(n+1)]
    #set as 1-ordered
    n2 = n2[1:]
    permuter([],n2)

def permuter(finalPerm, inputPerm):
    if len(inputPerm) == 0:
        print (finalPerm)
    else:
        for i in range(len(inputPerm)):
            recurPerm = operator.concat(finalPerm, inputPerm[i:i+1])
            rmainPerm = operator.concat(inputPerm[:i],inputPerm[i+1:])
            permuter(recurPerm,rmainPerm)

permuterDriver(int(input("n = ? ")))