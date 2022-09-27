def compareTriplets(alice_rating, bob_rating):
    score=[0,0]
    for i in range(3):
        if(alice_rating[i]>bob_rating[i]):
            score[0]+=1
        elif(alice_rating[i]<bob_rating[i]):
            score[1]+=1
    return score