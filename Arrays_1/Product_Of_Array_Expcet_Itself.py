#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]    #Initialize result array to 1
        
        for i in range(1, len(nums)):   #Continue till the length of the array and append the product of nums[i-1]*result[-1] into the result
            result.append(nums[i-1]*result[-1])
            
        rProd = 1   #Initialize rProd as 1
        for i in range(len(result)-2, -1, -1):  #For lenght of result-2 contnue from the last of the array
            result[i] *= nums[i+1]*rProd    #Store the product of result[i] * nums[i+1]*rProd into result[i]
            rProd *= nums[i+1]  #Multiply rProd to nums[i+1]
            
        return result   #Return the result
        