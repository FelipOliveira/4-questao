import time
import random
def counting_sort(array, maxval):
    """in-place counting sort"""
    #n = len(array)
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in array:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    return array

def preenche(array, n):
	for i in range(0, n):
		aux = random.randint(1, n)
		#print(aux)
		array.insert(0, aux)

arquivo = open("CoutingResult.txt","w")
arquivo.write("tamanho do vetor\ttempo decorrido(mseg)\n")
arquivo.close()

print("COUNTING=SORT=========================")

arquivo = open("CoutingResult.txt","a")

vet = []
#n = int(input("Quantos números no vetor?"))
i = 1000
#for i in range(10, 10000):
while(i<=10000):
	preenche(vet, i)
	maximo = max(vet)
	start = time.clock()
	counting_sort(vet, maximo)
	end = time.clock()

	tTotal = round(end-start,5)

	print(i,"- Tempo parcial:",tTotal,"Maior elemento:",maximo)
	
	arquivo.write("%d\t%f\n"%(i, tTotal))
	i += 1000
print("Terminado.")
arquivo.close()
