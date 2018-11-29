# Python program for implementation of heap Sort 

import random
import time
# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i): 
	largest = i # Initialize largest as root 
	l = 2 * i + 1	 # left = 2*i + 1 
	r = 2 * i + 2	 # right = 2*i + 2 

	# See if left child of root exists and is 
	# greater than root 
	if l < n and arr[i] < arr[l]: 
		largest = l 

	# See if right child of root exists and is 
	# greater than root 
	if r < n and arr[largest] < arr[r]: 
		largest = r 

	# Change root, if needed 
	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i] # swap 

		# Heapify the root. 
		heapify(arr, n, largest) 

# The main function to sort an array of given size 
def heapSort(arr): 
	n = len(arr) 

	# Build a maxheap. 
	for i in range(n, -1, -1): 
		heapify(arr, n, i) 

	# One by one extract elements 
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] # swap 
		heapify(arr, i, 0) 

def preenche(array,modo,n):
	if (modo==1):
		arquivo = open("HeapResultCres.txt","w")
		arquivo.write("tamanho do vetor\ttempo decorrido\n")
		arquivo.close()
		for i in range(1, n):
			aux = i
			#print(aux)
			array.insert(0, aux)
	elif (modo==2):
		arquivo = open("HeapResultDecres.txt","w")
		arquivo.write("tamanho do vetor\ttempo decorrido\n")
		arquivo.close()
		for i in range(1, n):
			aux = 100-i
			#print(aux)
			array.insert(0, aux)
	elif (modo==3):
		arquivo = open("HeapResultAle.txt","w")
		arquivo.write("tamanho do vetor\ttempo decorrido\n")
		arquivo.close()
		for i in range(1, n):
			aux = random.randint(1,n)
			#print(aux)
			array.insert(0, aux)

arr = []
arr2 = []
arr3 = []

arquivo = open("HeapResultCres.txt","a")

i = 100
while(i <= 5000):
	preenche(arr,1,i)
	
	start = time.clock()
	heapSort(arr)
	end = time.clock()

	tTotal = round(end-start,5)
	
	print(i,"- Tempo parcial:",tTotal)
	arquivo.write("%d\t%f\n"%(i, tTotal))
	i += 100

arquivo.close()
