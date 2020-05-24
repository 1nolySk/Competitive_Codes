"""
LeetCode Weekly Contest 190

Max Dot Product of Two Subsequences
https://leetcode.com/problems/max-dot-product-of-two-subsequences/

"""
class Solution:
    def maxDotProduct(self, nums1, nums2) -> int:
        
        # DP initialization, one row for previous and second for current max
        d  = [[-9999999 for i in range(len(nums2))] for j in range(2)]
        

        # Multiply each element of num1 to num2 elements and store in DP
        for i, j in enumerate(nums1):
            m_cur = -9999999
            for m,n in enumerate(nums2):
                
                # current index values product
                v = j*n

                # check for max product of num1 element in current num2
                if v>m_cur:
                    m_cur = v
                    
                # Add to max upto that index using DP
                if m>0 and d[0][m-1]+v >= v:
                    
                    d[1][m] = d[0][m-1] + v
                    
                    # Update current max
                    if d[1][m]>m_cur:
                        m_cur=d[1][m]
                        
                else:
                    d[1][m] = m_cur


                # Check if previous alone was maximum 
                if d[0][m] >d[1][m]:
                    d[1][m] = d[0][m]


                # Check for max in current range and update                    
                if m>0 and d[1][m]<d[1][m-1]:
                    d[1][m]= d[1][m-1]
            
            # Update Dp current to 0th row 
            for i in range(len(nums2)):
                d[0][i] = d[1][i]
                
                
        # Last index always has the largest
        return d[0][-1]


# Main method
if __name__ =='__main__':
	
	ob = Solution()

    # This is input arrays
	a = [2, -1, -2, 7]
	b = [3, 0, -6, 8]

	print(ob.maxDotProduct(a,b))

        