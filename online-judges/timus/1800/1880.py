def getNumInput():
    return int(input())

def getEigenvaluesInput():
    return [int(n) for n in input().split()]

p1_num = getNumInput()
p1_eigenvalues = getEigenvaluesInput()

p2_num = getNumInput()
p2_eigenvalues = getEigenvaluesInput()

p3_num = getNumInput()
p3_eigenvalues = getEigenvaluesInput()

def getCommon(list1, list2):
    i = 0
    j = 0
    common = []

    while (i != len(list1) and j != len(list2)):
        if list1[i] == list2[j]:
            common.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1

    return common

p1p2_eigenvalues = getCommon(p1_eigenvalues, p2_eigenvalues)
team_eigenvalues = getCommon(p1p2_eigenvalues, p3_eigenvalues)
print(len(team_eigenvalues))
