def factors(n):
    factor_list = []
    for i in range(1,n+1):
        if n%i==0:
            factor_list.append(i)
    return factor_list

print factors(17)
print factors(100)
print factors(111)


#Only factors are 1 and itelf
#1 is not prime [1] == [1,1]
def isprime(n):
    return(factors(n)==[1,n])

print isprime(17)
print isprime(19)

#Prime nos below note

def primeupto(n):
    primelist = []
    for i in range(1,n+1):
        if isprime(i):
            primelist.append(i)
    return primelist

print "Prime List"

print primeupto(100)
print primeupto(1000)

# First n primes we should use while loop. for defined set use for loop

def nprimes(n):
    (count,i,plist) = (0,1,[])
    while count < n:
        if isprime(i):
            (count,plist) = (count+1,plist+[i])
        i += 1
    return plist

print "Print N primes"

print nprimes(20)

# While to stimulate for
# for i in range(i,j)
#     statements
#
# n = i
# while n < j:
#     statements
#     n += 1
# for i in l:
#     statements
# i = 0
# while i < len(l):
#     n = l[i]
#     statement
#     i = i + 1
print range(10,1,-1)
