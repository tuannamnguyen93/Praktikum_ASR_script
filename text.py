def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)
 
    pre_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        cur_row = [i + 1]
        for j, c2 in enumerate(s2):
            ins = pre_row[j + 1] + 1
            dels = cur_row[j] + 1
            subs = pre_row[j] + (c1 != c2)
            cur_row.append(min(ins, dels, subs))
        pre_row = cur_row
 
    return pre_row[-1]
