def countApplesAndOranges(s, t, a, b, apples, oranges):
    number_apples,number_oranges=0,0
    for apple in apples:
        if(s<= (apple+a) <=t):
            number_apples+=1
    print(number_apples)        
    for orange in oranges:
        if( s<=(orange+b)<=t):
            number_oranges+=1        
    print(number_oranges)