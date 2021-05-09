def selection_soearch(L,x):
	n=len(L)
	
	for i in range(0,n-1):
		
		if L[i]==x:
			print(x, " is in position", i)
		else:
			print(x, "is not in the list", L)
			
		
	
if __name__ == "__main__":
	L=[3,4,321,6,9,8,7,1,5,37,19,28,42,15]
	selection_soearch(L,15)
