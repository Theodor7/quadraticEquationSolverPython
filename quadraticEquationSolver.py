from math import sqrt
print '\n*** QUADRATIC EQUATION SOLVER ***\n\nax^2 + bx + c = 0\n\nEnter a, b, and c:'

a = input('a = ')
b = input('b = ')
c = input('c = ')

d = b*b-4*a*c
print '\nDiscriminant = ' + str(d) +'\n'

if(d < 0):
    print 'NO SOLUTIONS'

if(d == 0):
    print '1 SOLUTION:\n' + str((-b)/(2*a))

if(d > 0):
    print '2 SOLUTIONS:\n' + str((-b-sqrt(d))/(2*a)) + ' and ' + str((-b+sqrt(d))/(2*a))
