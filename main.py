def find(a,b):
    
    n, m = a,b
    
    # n represents number of days for which we need to find possible ways
    # m represents the number of days of cosecustive absents
    # create  matrix with initial value 0
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    # print(dp)

    # assign value of 1 way to first row till 3 
    for i in range(m):
        dp[0][i] = 1
    # print(dp)

    # fill other cells of matrix
    for i in range(1, n + 1):
        for j in range(0, m):
            dp[i][j] = dp[i - 1][0] + dp[i - 1][j + 1]

    # print(dp)
    return str(dp[n-1][1])+"/"+str(dp[n][0]) 
    
n = int(input("Please insert number of Days : ")) # total number of days
m = 4 #4 and more consecutive days are not allowed
print("Output is : "+find(n,m))