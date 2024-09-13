
def makeAlpha():
    '''
    Makes a list with letters a-z
    '''
    letter = "a"
    myList = []
    while letter <= "z":
        myList.append(letter)
        letter = ord(letter) + 1
        letter = chr(letter)
    return myList
def linearSearch(haystack):
    for i in range(0,len(haystack)):
        l = haystack[i]
        answer = input("Is your letter "+l+"? ")
        if answer.lower()=="y":
            print("We found it!")
            return
    return
def binarySearch(haystack,start=None,stop=None):
    if start==None or stop==None:
        start = 0
        stop = len(haystack)-1
        binarySearch(haystack,start,stop)
        return
    if start > stop:
        print("Not Found!")
        return
    middle = start + (stop-start)//2
    print("Searching",haystack[start:stop+1])
    l = haystack[middle]
    answer = input("Is your letter "+l+"? (y,h,l) ")
    if answer.lower()=="y":
        print("We found it!")
        return
    if answer.lower()=="l":
        binarySearch(haystack,start,middle-1)
        return
    else:
        binarySearch(haystack,middle+1,stop)
        return
alpha = makeAlpha()
#linearSearch(alpha)
binarySearch(alpha)