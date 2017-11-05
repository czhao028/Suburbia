
with open('C:\\Users\czhao\Downloads\data\\ua_zcta_rel_10.txt') as txt:
    l = txt.read().splitlines()
    c = open("zip.csv", "w")
    for line in l:
        c.write(str(line)+"\n")
