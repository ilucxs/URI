#Váriaveis
N=[1,2,3,4,5,6,7,8,9,10]
V=int(input())

#Entrada
for i in range(0, len(N), 1):
     
    N[i] = V
    V = V * 2
   
    #Saída 
    print('N[{}] = {}'.format(i,N[i]))
