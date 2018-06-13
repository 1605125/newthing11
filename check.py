noprimes1 = [j for i in range(2, 10) for j in range(i*2, 100, i)]

prime = [i for i in range(2, 100) if i not in noprimes1]
print(noprimes1)
print(prime)
