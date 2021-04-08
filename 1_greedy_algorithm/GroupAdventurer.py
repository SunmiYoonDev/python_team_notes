'''
Find out how many adventurer groups can you make
Each adventurer has a fear level which shows a number of people to make a group.
eg. Someone has 3 fear level should join in more than group of 3.
input           output
2 3 1 2 2       2
'''
adventurers = list(map(int, input().split()))
adventurers.sort()

total_group = 0 # total number of groups
count = 0       # the number of adventurers in a group

for adventurer in adventurers:
    count += 1
    if count >= i:
        total_group += 1
        count = 0

print(total_group)
