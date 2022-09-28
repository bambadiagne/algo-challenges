def plusMinus(arr):
    n,pos_numbers,neg_numbers,zero_numbers=len(arr),0,0,0
    for number in arr:
        if(number>0):
            pos_numbers+=1
        elif(number<0):
            neg_numbers+=1
        else:
            zero_numbers+=1
    print(f'{pos_numbers/n:6f}')
    print(f'{neg_numbers/n:6f}')
    print(f'{zero_numbers/n:6f}')