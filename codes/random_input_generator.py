from random import randint
k=50
def sparse(d):
	y=[]
	count=0
	for i in range(0,d):
		temp=randint(0,1)-randint(0,1)
		if temp==-1:
			temp=0
		y.append(temp)
		if y[i]==1:
			count = count+1
		if count==k :
			break
	while (i<d-1):
		y.append(0)
		i = i+1
	return y

if __name__ == '__main__':
	list = sparse(1000)
	file = open('input.txt', 'w')
	for item in list:
		file.write("%s\n" %(item))
	

