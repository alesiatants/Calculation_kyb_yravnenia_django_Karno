import math
def calculation(a,b,c,d):
	p = (3*a*c - b**2)/(3*a**2)
	q = (2*b**3 - 9*a*b*c + 27*a**2*d)/(27*a**3)
	S = q**2/4 + p**3/27
	if S > 0:
		r = -q/2 + math.sqrt(S)
		s = -q/2 - math.sqrt(S)
		u = r**(1/3) if r >= 0 else -(-r)**(1/3)
		v = s**(1/3) if s >= 0 else -(-s)**(1/3)
		x1 = u + v - b/(3*a)
		x2 = -(u + v)/2 - b/(3*a) + (u - v)*math.sqrt(3)/2j
		x3 = -(u + v)/2 - b/(3*a) - (u - v)*math.sqrt(3)/2j
		return x1, x2, x3
	elif S == 0:
		if q >= 0:
			x1 = -2*q**(1/3) - b/(3*a)
			x2=x3 = q**(1/3) - b/(3*a)
			
		else:
			x1 = q**(1/3) - b/(3*a)
			x2 = x3 = -(q**(1/3) + b/(3*a))/2
			return x1, x2, x3
	else:
		alpha = (-q/2 + S**(1/2))**(1/3)
		beta = (-q/2 - S**(1/2))**(1/3)
		x1 = alpha + beta - b/(3*a)
		x2 = -(alpha + beta)/2 - b/(3*a) + (alpha - beta)*math.sqrt(3)/2j
		x3 = -(alpha + beta)/2 - b/(3*a) - (alpha - beta)*math.sqrt(3)/2j
		return x1, x2, x3