def kangaroo(x1, v1, x2, v2):
    if((v1==v2) or (v2>v1)):
        return "NO"
    return "YES" if((x2-x1)%(v1-v2)==0) else "NO"