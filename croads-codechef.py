'''

Codechef - MayCook Off 2020
Roads in Chefland - https://www.codechef.com/COOK118B/problems/CROADS

'''

# Function to check if perfect power of 2
def isPowerOfTwo (x): 

    return (x and (not(x & (x - 1))) ) 

   
def solve(a):
    
    # If perfect power of 2 road cannot be constructed
    if isPowerOfTwo(a):
        return -1
    
    c = 0   # store total cost
    i = 0   # power value iterator
    while(a>0):
        
        d = math.ceil(a/2)  # Find power of by n/2
        c += pow(2, i)*d    # Cost value is leftmost bit position value
        a = a//2            # Update a by dividing by 2
        i+=1                # power iterator increament

        
    return c-1              # -1 since 1 is always in path, so exclude its cost
        

# Main method, Inputs
t = int(input())
for _ in range(t):
    
    a = int(input())
    
    print(solve(a))