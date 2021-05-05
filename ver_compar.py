def ver_compare(ver1, ver2):
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
            
        
    
print(ver_compare((input().split('.')), (input().split('.'))))
