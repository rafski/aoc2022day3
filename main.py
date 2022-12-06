import string

import numpy
from collections import Counter

with open('input.txt') as f:
    inputs = f.read().splitlines()
    rucksacks = numpy.array(inputs)
    priority_sum = 0
    team_priority_sum = 0
    for sack in rucksacks:
        firstpart, secondpart = sack[:len(sack) // 2], sack[len(sack) // 2:]
        # print(firstpart)
        # print(secondpart)
        common_parts = list(set(firstpart) & set(secondpart))
        #print(common_parts)
        for part in common_parts:
            for part in common_parts:
                priority = 0
                if part.islower():
                    priority = ord(part) - 96
                    # print(priority)
                else:
                    priority = ord(part) - 64 + 26
                    # print(priority)
                priority_sum += priority
    print(priority_sum)

    teams = numpy.array_split(rucksacks, len(rucksacks)/3)
    #print(teams[1])
    for team in teams:
        team_letter_0 = ''.join(set(team[0]).intersection(team[1]))
        team_letter = ''.join(set(team_letter_0).intersection(team[2]))
        print(team_letter)
        for letter in team_letter:
            team_priority = 0
            numpy.array(letter)
            #print(letter)
            if letter.islower():
                team_priority = (ord(letter) - 96)
            else:
                team_priority = (ord(letter) - 64 + 26)
            team_priority_sum += team_priority
    print(team_priority_sum)