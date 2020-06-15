'''

Codechef - June Long Challenge 2020
The Tom and Jerry Game! - https://www.codechef.com/JUNE20B/problems/EOEO

'''

def solve(n):
    
    # Reduce n until it becomes odd
    while(n%2 == 0 and n>0):
        
        n = n//2
    
    # If n==0, which will not happen acc to question
    if n==0:
        return 0
    
    # Return integer division of 2 i.e No of ways
    return n//2


t = int(input())
for _ in range(t):
    
    n = int(input())
    
    res = solve(n)
    
    print(res)