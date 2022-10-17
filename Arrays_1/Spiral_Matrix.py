#Time_Complexity: O(m*n)
#Space_Complexity: O(m*n)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) #Lenght of the rows
        n = len(matrix[0])      #Lenght of the columns
        
        left = 0
        right = n-1
        top = 0
        bottom = m-1
        
        result = [] #Initialize result as an emoty array
        
        while left<=right and top<=bottom:  #Continue till left, right and top, bottom doesn't cross each other
            #Left to Right
            for i in range(left, right+1):
                result.append(matrix[top][i])   ##Append the values in the result as mat[top][i] all the elements in the top row
            top +=1 #Increment top by 1
            #Top to Bottom    
            for j in range(top, bottom+1):  
                result.append(matrix[j][right]) #Append the values in the result as mat[j][right] all the elements in the right column
            right-=1
            
            if len(result) == m*n:  #If the length of the result is equal to m*n then break the loop
                break
            
            #Right to Left
            for k in range(right, left-1, -1):
                result.append(matrix[bottom][k])     #Append the values in the result as mat[bottom][k] all the elements in the bottom row
            bottom -=1
                
            #Bottom to Top
            for l in range(bottom,top-1, -1):
                result.append(matrix[l][left])  #Append the values in the result as mat[l][left] all the elements in the left column
            left+=1
                
        return result   #Return the result