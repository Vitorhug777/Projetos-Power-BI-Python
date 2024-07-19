import numpy as np
lista=[0,1,2,3,4,5,6,7,8]
def calculate(lista):
    lista = np.reshape(lista, (3,3))
    dicionário={'mean': [[float(np.mean(lista[0:3,0])),float(np.mean(lista[0:3,1])),float(np.mean(lista[0:3,2]))],
                         [float(np.mean(lista[0,0:3])),float(np.mean(lista[1,0:3])),float(np.mean(lista[2,0:3]))],
                         float(np.mean(lista.flatten()))],

                'variance': [[float(np.var(lista[0:3,0])),float(np.var(lista[0:3,1])),float(np.var(lista[0:3,2]))],
                            [float(np.var(lista[0,0:3])),float(np.var(lista[1,0:3])),float(np.var(lista[2,0:3]))],
                            float(np.var(lista.flatten()))],

                'standard deviation': [[float(np.std(lista[0:3,0])),float(np.std(lista[0:3,1])),float(np.std(lista[0:3,2]))],
                            [float(np.std(lista[0,0:3])),float(np.std(lista[1,0:3])),float(np.std(lista[2,0:3]))],
                            float(np.std(lista.flatten()))],     

                'max': [[int(np.max(lista[0:3,0])),int(np.max(lista[0:3,1])),int(np.max(lista[0:3,2]))],
                            [int(np.max(lista[0,0:3])),int(np.max(lista[1,0:3])),int(np.max(lista[2,0:3]))],
                            int(np.max(lista.flatten()))],

                'min': [[int(np.min(lista[0:3,0])),int(np.min(lista[0:3,1])),int(np.min(lista[0:3,2]))],
                            [int(np.min(lista[0,0:3])),int(np.min(lista[1,0:3])),int(np.min(lista[2,0:3]))],
                            int(np.min(lista.flatten()))],
                            
                'sum': [[int(np.sum(lista[0:3,0])),int(np.sum(lista[0:3,1])),int(np.sum(lista[0:3,2]))],
                            [int(np.sum(lista[0,0:3])),int(np.sum(lista[1,0:3])),int(np.sum(lista[2,0:3]))],
                            int(np.sum(lista.flatten()))]
                            
                            
                }
            
    print(lista)
    print(dicionário)



calculate(lista)
