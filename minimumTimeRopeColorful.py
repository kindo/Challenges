
"""
Leetcode 1578: Minimum Time to Make Rope Colorful

Problem description: 

Alice has n balloons arranged on a rope. 
You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. 
She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.


"""
# Greddy solution with O(n) time complexity and O(1) space complexity 
#runing time beats 93% of python submission 
#memory usage beats 71% of python submission 

def minCost(colors: str, neededTime:list) -> int:

    minTime = []
    for i in range(len(colors)-1):

        if colors[i] == colors[i+1]:
            if neededTime[i] < neededTime[i+1]:
                t = neededTime[i]
                minTime.append(t)
            else:
                t = neededTime[i+1]
                neededTime[i+1] = neededTime[i]

                minTime.append(t)
    return sum(minTime)

c = "aaabbbabbbb"
nt = [3,5,10,7,5,3,5,5,4,8,1]

(print("The minimum time Bob needs to make the rope colorful:", 
       minCost(c, nt)))
