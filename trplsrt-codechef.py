# Codechef May20 Long Challenge
# Question Link - https://www.codechef.com/MAY20B/problems/TRPLSRT

def solve(a, n, k):
    
    # mark the indices that needs swapping as False
    vis = [True if i==a[i]-1 else False for i in range(n)]
    
    ans = 0 # count
    res = [] # storing the output to print
    two = [] # storing the indices in case of even length
    for ind in range(n):
        
        if vis[ind]:
            # if travelled skip to next index
            continue
        
        j = ind
        count = 0
        s = []
        # this generates each cycle
        while vis[j]==False:
            s.append(j)
            vis[j] = True
            j = a[j]-1
                        
            count += 1

        if count%2!=0:
            # For odd length cycle
            ans += count//2
            # Logic to generate all pair of 3 indices
            for p in range(1, count//2 + 1):
                res.append([s[0]] + s[p*2 -1 : 2*p+1])
            
        else:
            # For even length cycle
            ans += (count//2 -1)
            # Cycle until only 2 will be left
            for p in range(1,count//2):
                res.append([s[0]] + s[p*2 - 1: 2*p + 1])  
            
            # Store the 2 indices
            two += [s[0], s[-1]]
            # When we get 2 odd cycle we can solve in 2 steps
            if len(two)>2:
                ans += 2
                
                res.append(two[:3])
                res.append([two[0], two[3], two[2]])
                two.clear()
        # If greater than k return -1
        if ans>k:
            return [-1, []]

    # In case there is even cycle left, so return -1
    if len(two)>0:
        return [-1, []]
    
    return [ans, res]

#================================================
# main 
t = int(input())

for _ in range(t):
    
    n, k = map(int, input().split())
    
    a = list(map(int, input().split()))
    
    count, s = solve(a,n,k)
    
    # printing output
    print(count)
    for i in s:
        t = [j+1 for j in i]
        print(*t)