""" We can approach this question using a brute force approach , iterating over each element of the array intitially, then nesting another loop to iterate over the loop again to sum all possible pairs. This is not a scalable solution as it runs in 0(n^2) complexity"""

def findTargetSum(arr,target):

  for e in range(len(arr)-1):
    for j in range(e+1,len(arr)-1):
      newSum = arr[e] + arr[j]
      if newSum == target:
        return (f' pair {arr[e],arr[j]} = the target of {target}')
  
      
  return ("No pairs found") 




def findTargetSum2(arr,target):
  ''' empty dictionary called numbersChecked, a empty variable to store the complement of current element as goalNumber,
   loop through each element and see if it is a value in the dictionary, if so return the element and its complement(stored as goalNumber), if not add the element and its complement to the dictionary, 
   if at end of the loop, return false'''

  numbersChecked = dict() # 0(n)
  for e in arr: # 0(n)
    goalNumber = (target-e)# 0(1)
    if e in numbersChecked.values():# 0(1) (given no collisions)
      return (e,goalNumber ) # 0(1)
    elif e in numbersChecked.keys(): # 0(1) (avoid collisions)
      pass
    else:
      numbersChecked.update({e:goalNumber}) # 0(1) (given no collisions)

  return ("No pairs found") # 0 (1)


# This solution has a 0(n) time complexity



  


print(findTargetSum2([1,23,1,4,3,2,5,67,0],23))