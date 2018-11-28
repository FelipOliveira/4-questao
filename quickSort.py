# Python program for implementation of Quicksort Sort 

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot
import time
import random

def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low,high): 
	if low < high: 

		# pi is partitioning index, arr[p] is now 
		# at right place 
		pi = partition(arr,low,high) 

		# Separately sort elements before 
		# partition and after partition 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high)
		
def preenche(array, n):
	for i in range(0, n):
		aux = random.randint(1, n)
		#print(aux)
		array.insert(0, aux)

arquivo = open("QuickResult.txt","w")
arquivo.write("tamanho do vetor\ttempo decorrido\n")
arquivo.close()

print("QUICK=SORT=========================")

arquivo = open("QuickResult.txt","a")

vet = []
#n = int(input("Quantos números no vetor?"))
i = 10
#for i in range(10, 10000):
while(i<5010):
	preenche(vet, i)
	n = len(vet)
	start = time.clock()
	quickSort(vet,0,i-1)
	end = time.clock()

	tTotal = round(end-start,5)
	
	print(i,"- Tempo parcial:",tTotal)
	
	arquivo.write("%d\t%f\n"%(i, tTotal))
	i += 10
print("Terminado.")
arquivo.close()

# This code is contributed by Mohit Kumra 
