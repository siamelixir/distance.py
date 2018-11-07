import math

v0 = int(input())
a = int (input())
dt = 0.3
t = 0
while  t <= 5:
	
	s = v0*t + 0.5*a* sqrt(t)
	print('time = %.3f' % t,'dt = %.2f' % s)

	t = t + dt
