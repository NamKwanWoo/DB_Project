def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

for internalID in range(1,200):
    mangled = (internalID*1679979167)%(36**6)
    print (internalID, mangled, baseN(mangled,36))