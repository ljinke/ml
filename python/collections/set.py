#just like set in math: a unique collection of items - no duplicated items
a= [1,2,3,4,5,6,1,1,1]
sA = set(a)

print sA

sB = set([4,5,6,2,7])
 

print sA - sB #
print sA & sB #intersection
print sA | sB #union