def printMe(msg='No message was provided'):
	print(msg)


def printList(L=[]):
	for x in L:
		print(x)


def checkIfNum(*args):
	for x in args:
		if not(isinstance(x, (int, float))):
			return False
	return True


def checkIfNumList(L):
	for x in L:
		if not(isinstance(x, (int, float))):
			return False
	return True


def findMinStr(L, startIndx):
    m = L[startIndx]
    idx = startIndx
    for i in range(startIndx, len(L)):
        x = L[i]
        if x < m:
            m = x 
            idx = i
        else:
            pass 
    return m,idx 


def swapValues(L, idx1, idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L


