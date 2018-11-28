def funcao(num):
	sign = int(num[0],2)
	exp = int(num[1:9],2)
	fraction = num[8:]
	bias = 127
	mantissa = 0
	
	for i in range(23,0,-1):
		if fraction[i] == '1':
			#print("frac:",mantissa)
			mantissa += 2**(-i)
			
	print("signal:",sign,"expoente:",exp,"mantissa",mantissa)
	
	if exp == 0:
		if mantissa == 0:
			return 0.0
		else:
			return (-1)**sign * mantissa * 2**(exp - (bias-1))
	elif exp == 255:
		if mantissa == 0:
			return float('inf')
		else:
			return float('NaN')
	else:
		return (-1)**sign * (1 + mantissa) * 2**(exp - bias)
	
#value = "00111111100000000000000000000000"	#0
#value = "01000000010010010000111111011011"	#3.1415
#value = "00111111100000000000000000000000"	#1
#value = "00111110101010101010101010101011" #1/3
value = "01111111011111111111111111111111"	#maior inteiro
print(funcao(value))
