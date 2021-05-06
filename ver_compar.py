def ver_compare(ver1, ver2):
    
    if not(isinstance(ver1, str) and isinstance(ver2, str)): 
        raise TypeError('ver must be str')

    if ver1 == '' or ver2 == '':
        raise ValueError('ver must contain at least one number')

    ver1 = ver1.split('.')
    ver2 = ver2.split('.')
    
    for i in (ver1 + ver2):
        if not(i.isdigit()):
            raise ValueError("ver can't contain anything other than numbers and a dot")
    
    ver1 = [int(x) for x in ver1]
    ver2 = [int(x) for x in ver2]
    
    if len(ver1) > len(ver2):
        max = len(ver1)
        while len(ver1) > len(ver2):
            ver2.append(0)
    else:
        max = len(ver2)
        while len(ver2) > len(ver1):
            ver1.append(0)
    
    for i in range(max):
        if ver1[i] > ver2[i]:
            return 1
        elif ver1[i] < ver2[i]:
            return -1
    return 0
               
print(ver_compare(input(), input()))