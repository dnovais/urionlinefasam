def is_prime(n):
	flag = 0
	result = 0
	while (flag <= n):
			flag += 1
			if (n % flag == 0):
					result += 1

	if (result == 2):
			return True
	return False

cases = int(input())
vector = []
counter = 0

while(counter < cases):
	number = int(input())
	vector.append(number)
	counter = counter + 1

for i in vector:
  if(is_prime(i)):
    print(str(i) + " eh primo")
  else:
    print(str(i) + " nao eh primo")
