def superDigit(n, k):
    if(len(n)==1):
        return int(n)
    sum_digits=sum(int(dig) for dig in n)
    return superDigit(str(sum_digits*k),1)