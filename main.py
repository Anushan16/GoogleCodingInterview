# We can approach this question using a brute force approach , iterating over each element of the array intitially, then nesting another loop to iterate over the loop again to sum all possible pairs. This is not a scalable solution as it runs in 0(n^2) complexity
'''
def findTargetSum(arr,target):

  for e in range(len(arr)-1):
    for j in range(e+1,len(arr)-1):
      newSum = arr[e] + arr[j]
      if newSum == target:
        return (f' pair {arr[e],arr[j]} = the target of {target}')
  
      
  return ("No pairs found") '''




def findTargetSum2(arr,target):
  ''' empty dictionary called numbersChecked, a empty variable to store the complement of current element as goalNumber,
   loop through each element and see if it is a value in the dictionary, if so return the element and its complement(stored as goalNumber), if not add the element and its complement to the dictionary, 
   if at end of the loop, return false'''

  numbersChecked = dict()
  for e in arr:
    goalNumber = (target-e)
    if e in numbersChecked.values():
      return (e,goalNumber ) 
    else:
      numbersChecked.update({e:goalNumber})
  return ("No pairs found")




  


print(findTargetSum2([1,23,4,3,2,5,67,54],23))