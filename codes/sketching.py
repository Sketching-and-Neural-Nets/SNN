
from random import randint

p= 2**61 -1
d=1000
m=150
'''
define a,b,d,m here...
d= input dimension
m=output dimension


'''


def sketch(x,a,b):
	y=[]
	for l in range(0,m):
		temp=0
		for i in range(0,d):
			if(x[i] and hash(i,a,b)==l):
				temp=1
				break
		y.append(temp)
	return y


def hash(i,a,b):
	"outputs the hash value of the input key"
	pass
	return ((a*i+b)%p)%m


if __name__ == '__main__':
	#result = {}
	result = []
	x=[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
	x=50*x
	for h in range(0,20):
		a=randint(1,p-1)
		b=randint(1,p-1)
		print(a,b)
		result.append(sketch(x,a,b))
	for i in range(0,m):
		print("%s"%(result[0][i]))

#sketch of input vectors stored in 'result'