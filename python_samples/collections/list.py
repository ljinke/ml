#list is an ordered collection of objects.
#have anything in a list
jj=[]
jj.append(1)
jj.append('nice hat')

print jj

a = [1,2,2,2,5,6,0,1,5]
myList = [item*4 for item in a]

print myList

myList2 = [item*4 for item in a if item > 2]

print myList2