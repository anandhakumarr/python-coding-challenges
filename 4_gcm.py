def gcm(m,n):

    fm = []
    for i in range(1,m+1):
        if (m%i)==0:
            fm.append(i)

    fn = []
    for j in range(1,n+1):
        if n%j==0:
            fn.append(j)

    cf = []
    for i in fm:
        if i in fn:
            cf.append(i)
    return cf[-1]

print gcm(101,3)
