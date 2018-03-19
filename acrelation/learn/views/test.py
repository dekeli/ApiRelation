__author__ = 'Administrator'
print("123")
newlist = [6, 5, 23, 4, 9, 6, 12, 36, 1, 8, 7]
i = 0
while i < len(newlist)-1:
    j = i+1
    i += 1
    while j > 0:
        if newlist[j] < newlist[j-1]:
            temp = newlist[j-1]
            newlist[j-1] = newlist[j]
            newlist[j] = temp
            j -= 1
        else:
            break


print(newlist)
