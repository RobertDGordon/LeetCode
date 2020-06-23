# // You hired a neighborhood kid to help paint your fence in a white and black striped pattern. However, they didn't do the best of jobs; they sometimes painted the same color multiple planks in a row. What's the minimum number of planks you need to repaint so that planks always alternate?

# // Sample 1 input: [0, 1, 0, 1]
# // Sample 1 output: 0, no repainting required.

# // Sample 2 input: [0, 1, 0, 0, 1]
# // Sample 2 output: 2, since you would need to modify 2 planks to get to correctly striped state [0, 1, 0, 1, 0]

# /**
#  * @param {number[]} planks
#  * @return {number}
#  */
 
#  [0,1,0,1,0]
 
#  [1,1,0,1,0*]
#   e o e o e
#    first = 1
#    count1 = 4
#    count2 = 1
#  set var first to 1
#  loop over each element
#      if element is %2 = 0: (even)
#          check if element is NOT equal first value<<
#              increment count1
#      else:
#          check if element is equal to first value
#              increment count1
 
#  set var first to 0 <<
#  loop over each element
#      if element is %2 = 0: (even)
#          check if element is NOT equal first value
#              increment count2
#      else:
#          check if element is equal to first value
#              increment count2
#  if count1 < count2:
#     return count1
#  else:
#     return count2
 
 
 
#  def count_planks(arr):
#      count1 = 0
#      count2 = 0
#      first1 = 1
#      first0 - 0
#      for i in range(len(arr)):
#          if (arr[i]%2) == 0:
#              if arr[i] != first1:
#                  count1 += 1
#              elif arr[i] != first0: <<combine two loops and check for both at the same time.
#                  count2 += 1
#          else:
#              if arr[i] == first:
#                  count1 += 1
#      first = 0
#      for i in range(len(arr)):
#          if (arr[i] %2) == 0:
#              if arr[i] != first:
#                  count2 += 1
#          else:
#              if arr[i] == first:
#                  count2 += 1
#      if count1 < count2:
#          return count1
#      else:
#          return count2



