# Make randomly person data

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

print ("ID, personal_Phone, e-mail")

for internalID in range(1,21):
    mangled = (internalID*1679979167)%(36**6)
    #print (internalID, mangled + (internalID*167997)%(36**3), baseN(mangled,36) + '@' + baseN(mangled,36) + '.com')
    print(mangled%10000)
