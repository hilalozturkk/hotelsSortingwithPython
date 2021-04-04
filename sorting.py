
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import re


df = pd.read_csv('chennai_reviews.csv') #data set okuma
df.head()


liste = df["Hotel_name"] #otel isimlerini listeleme
print(liste)



hotels = []
x=1
while x<len(liste):   
    
        if df["Hotel_name"].loc[x] != df["Hotel_name"].loc[x-1] :  #kaç tane farklı otel olduğunu bulma
             hotels.append(df["Hotel_name"].loc[x-1])
         
        x += 1



i=0
for x in hotels:     #kaç tane farklı otel olduğunu yazdırma
     print(i ,"\t", x, "\n")
     i += 1



#m=df["Review_Text"].isin(["good"])
#df[m]
#df = df['Review_Text'].values
#df = df.reshape(-1,1)
#print(df.shape)
#df[:4724]
#a= np.array(df)

#print(a)




m=df["Review_Text"]   #Review_Text colonunu atama



i = 0
toplam = 0

liste2 = df["Hotel_name"]
liste3 = []
for x in m :
    text = x   #tüm yorumları dolaşma
    search_great = "(Good?)|(good?)"   
    search_great_counter = 0

    search_helpful = "(Helpful?)|(helpful?)"
    search_helpful_counter = 0
    
    search_excellent = "(Excellent?)|(excellent?)"
    search_excellent_counter = 0
   
    for match in re.finditer(search_great,text): #örnek kelimeleri bulma
        search_great_counter += 1
        print(match)
        print(search_great_counter)
        print(liste2[i]) 
        liste3.append(liste2[i]) 
        toplam = toplam + 1
        
    for match in re.finditer(search_helpful,text): #örnek kelimeleri bulma
        search_helpful_counter += 1
        print(match)
        print(search_helpful_counter)  
        print(liste2[i]) 
        liste3.append(liste2[i]) 
        toplam = toplam + 1
    
    for match in re.finditer(search_excellent,text):
        search_excellent_counter += 1
        print(match)
        print(search_excellent_counter)
        print(liste2[i]) 
        liste3.append(liste2[i]) 
        toplam = toplam + 1
        
    i = i+1   
    


print("positive commit = ")   #bulduğumuz tüm pozitif yorumlar
print(toplam)



i=0
for x in liste3: 
        print(i)
        print(liste3[i])
        i = i+1




from collections import Counter
otelSayisi = []
x=0
while x<len(liste3):
    
        if liste3[x] != liste3[x-1] :    
             otelSayisi.append(liste3[x])
             
        x =x + 1
        

        
i=0
for x in otelSayisi:
     print(i ,"\t", x, "\n")
     i += 1
        
        
        
c = Counter(liste3)  
dict(c)   #array içinde bulunan tüm elamanlardan  kaç tane olduğunu sorgular       
        
    
    
 
sorted(c) # en fazla sayıda elemanı olandan en küçüğe sıralama
print(c)

