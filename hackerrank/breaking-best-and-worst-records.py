def breakingRecords(scores):
    n=len(scores)
    break_list,max_score,min_score=[0,0],scores[0],scores[0]
    for i in range(1,n):
        if(scores[i]>scores[i-1] and max_score<scores[i]):
            break_list[0]+=1
            max_score=scores[i]
        elif(scores[i]<scores[i-1] and min_score>scores[i]):
            break_list[1]+=1
            min_score=scores[i]
    return break_list 