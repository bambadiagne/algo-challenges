def birthday(s, d, m):
    n,count_div=len(s),0
    for i in range(1,n+1):
      if(sum(s[(i-1):i*m][:m])==d):
          count_div+=1
    return count_div