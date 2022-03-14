import sys

temp = [73,74,75,71,69,72,76,73]


def dailyTemperatures(temp):
    ans = [0] * len(temp) # initialize ans with 0s to prevent index error
    stack = []  # initialize stack

    for i, t in enumerate(temp):

        while stack and t > temp[stack[-1]]:
            d = stack.pop()
            ans[d] = i - d
        stack.append(i)
    return ans

print(dailyTemperatures(temp))