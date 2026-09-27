"""
for making dictionary we have 2 option
1st :- dictionary = dict()
2nd :- dictionary = {}
"""
num = [5,6,7,7,1,9,111,1,1,5,1,1]
freq_map = { }
for i in range(0, len(num)):
    if num[i] in freq_map :
        freq_map[num[i]] += 1
    else:
        freq_map[num[i]] = 1
print(freq_map[1])