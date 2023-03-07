import os
import pdf_compressor as compress
import time

# assign directory
directory = 'PDFs'

while True:
    time.sleep(6)
    print("Procurando arquivos...") 

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print(f) 
            fcompr = (f.replace(".pdf" , "_compr.pdf" , 3))
            if os.path.isfile(fcompr):
                print ("O arquivo já existe, abortando: " + fcompr)
                break
            else:
                print ("Convertendo arquivo: " + f)
                print ("Destino: " + fcompr)
                compress.compress(f, fcompr, power=4)
