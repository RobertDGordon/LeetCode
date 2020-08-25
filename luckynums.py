class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        #extract each array as a row
        #loop over row_array and find the min
        #
 
        row_arr = []
        min_num = None
        for row in matrix:
            row_arr = row
            for row_something in row_arr:
                next_num = row_arr[+1]
                if row_something < next_num:
                    min_num = row_something

        col_num = []
        for i in range(len(row_arr)):
            col_num = row_arr
            if min_num in col_num:
                return [min_num]
        
        
        
#         3  7  8 min = 3
#         9  11 13 min = 9
#         15 16 17 min = 15
        
#         7 8
#         1 2