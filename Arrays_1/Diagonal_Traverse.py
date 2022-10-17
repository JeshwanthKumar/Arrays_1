#Time_Complexity: O(m*n)
#Space_Complexity: O(m*n)

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m = len(mat)    #m is the length of the rows
        n = len(mat[0]) #n is the length of the columns
        result = [0]* (m*n) #Initialize a result array as 0s for m*n
        flag = 1    
        index = 0
        
        r = 0   #Initially set rows and column as 0
        c = 0
        
        while index<len(result):    #Continue till the length of the result
            result[index] = mat[r][c]   #Initalize result[index] as mat[r][c]
            
            if flag == 1:   #If flag is 1 then move downwards
                if c == n-1:    #If the index is in the last column then increment the row by 1 and change the flag to -1
                    r+=1
                    flag = -1
                elif r == 0:    #If the index is in the fitst row increment the column by 1 and change the flag to -1
                    c+=1
                    flag = -1
                else:   #Else decrement the row by 1 and increment the column by 1 
                    r-=1
                    c+=1
                    
            else:   
                if r == m-1: #Else if the index is in the last row increment the column by 1 and change the flag to 1
                    c+=1
                    flag = 1
                elif c == 0:    #If the index is in the first column increment the row by 1 and change th flag to 1
                    r+=1
                    flag = 1
                else:   #Else increment row by 1 and decrement the column by 1
                    r+=1
                    c-=1
            index+=1    #Increment the index in every iteration
            # print(index)  
        return result   #Return the result