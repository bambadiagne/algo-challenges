def getTotalX(a, b):
    min_intervalle,max_intervalle,count=min(a+b),max(a+b),0
    print(min_intervalle,max_intervalle)
    for number in range(min_intervalle,max_intervalle+1):
        is_valid=True
        for i in a:
            if(number%i!=0):
                is_valid=False
                break   
        for i in b:
            if(i%number!=0):
                is_valid=False
                break
        if(is_valid):
            count+=1         
    return count