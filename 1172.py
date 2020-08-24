#Váriaveis
X=[1,2,3,4,5,6,7,8,9,10]

#Entrada
for i in range(0, len(X), 1):
    X[i]=int(input())
    if X[i] <=0:
        X[i] = 1
    #Saída 
    print('X[{}] = {}'.format(i,X[i]))
