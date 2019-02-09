#PROMPT: Find the Kth smallest/largest element in an unsorted array, return a single integer

#ALWAYS start with clarifying Questions:
#Ints only?
#    Yes
#Space or Time restrictions:
#   1st solution no/2nd solution yes
#Will there be duplicates = assume no duplicates, followup yes duplicates
#Can we use built in functions like sort()?
#   yes, better to write your own
#Can we use data structures: YES
#Can we mutate OG list? Sure
#Can we look stuff up? Yes

#simplest, sort using built in function, from smallest to biggest, then count
def kth_smallest(k, array):
    #sort
    print(array)
    array.sort()
    #count
    print(array[k-1])
    return array[k-1]

#from biggest to smallest using built-in function, then count

def kth_largest(k, array):
    #sort
    array.sort(reverse = True)
    #count
    print(array[k-1])
    return array[k-1]


#RUN
k = 1
array = [3,4,1,2]
kth_smallest(k, array)
kth_largest(k, array)
