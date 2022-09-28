def superReducedString(s):
    letters=list(s)
    n=len(s)
    i=1
    while(i<n):
        if(letters[i]==letters[i-1]):
            del letters[i]
            del letters[i-1]
            n-=2
            i=0
        i+=1    
    return "Empty String" if letters==[] else "".join(letters)