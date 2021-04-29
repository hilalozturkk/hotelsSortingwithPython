#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd


# In[92]:


veri_seti = pd.read_csv('chennai_reviews.csv') #veri setini okuduk
veri_seti.head()               #veri setinin ilk 5 elemanını gösterdik


# In[93]:


hotel_name_verileri = veri_seti["Hotel_name"]   #  Hotel_name  sütununu hotel_name_verileri değişkenine atadık

farkli_otel_sayisi = []
x=1
while x<len(hotel_name_verileri):   # kaç farklı otel olduğunu bulundu
    
        if veri_seti["Hotel_name"].loc[x] != veri_seti["Hotel_name"].loc[x-1] :       
             farkli_otel_sayisi.append(veri_seti["Hotel_name"].loc[x-1])
         
        x += 1



i=0
for x in farkli_otel_sayisi:     #farklı tüm otelleri yazdırıldı
     print(i ,"\t", x, "\n")
     i += 1


# In[94]:


yorumlar = veri_seti['Review_Text'].apply(str)   
# Review_Text sütundaki verileri string olarak uygulayıp yorumlar değişkenine attık


# In[95]:


import re      # regEx kütüphanesinin import ettik kelime seçimi için
i = 0

pozitif_kelime_toplam = 0
negatif_kelime_toplam = 0 


tum_otel_isimleri = veri_seti["Hotel_name"] #Hotel_name sütununu al
pozitif_yorumlar = []
negatif_yorumlar = []

for x in yorumlar :                        # m değişkenini döndürüyoruz
        text = x                    
        
        good_ara = "(?i)good"   # (?i) -> case insensitive  (regEx kullandıldı kelimeleri seçmek için)
        good_sayac = 0

        clean_ara = "(?i)clean"
        clean_sayac = 0
        
        nice_ara = "(?i)nice"
        nice_sayac = 0
        
        helpfull_ara = "(?i)helpful*"
        helpfull_sayac = 0
        
        great_ara = "(?i)great"
        great_sayac = 0
        
        friendly_ara = "(?i)friendly"
        friendly_sayac = 0
        
        well_ara = "(?i)well"
        well_sayac = 0
        
        excellent_ara = "(?i)excellent"
        excellent_sayac = 0
        
        comfortable_ara = "(?i)comfortable"
        comfortable_sayac = 0
        
        best_ara = "(?i)best"
        best_sayac = 0
        
        for match in re.finditer(good_ara,text):  # regEx kütüphanesinden finditer() fonk. kullandık 
            good_sayac += 1              # belli bir text içinde aranan kelimeyi match etmeyi sağladık 
            print(match)
            print(good_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])              # pozitif_yorumlar hangi otelde kaç  pozitif kelimenin bulunduğunu 
                                                  # atadığımız hotel_name_verileri
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1     #tüm pozitif toplamı görmek için
        
        for match in re.finditer(clean_ara,text):
            clean_sayac += 1
            print(match)
            print(clean_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1

        for match in re.finditer(nice_ara,text):
            nice_sayac += 1
            print(match)
            print(nice_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1

        for match in re.finditer(helpfull_ara,text):
            helpfull_sayac += 1
            print(match)
            print(helpfull_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1

        for match in re.finditer(great_ara,text):
            great_sayac += 1
            print(match)
            print(great_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1

        for match in re.finditer(friendly_ara,text):
            friendly_sayac += 1
            print(match)
            print(friendly_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1

        for match in re.finditer(well_ara,text):
            well_sayac += 1
            print(match)
            print(well_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1


        for match in re.finditer(excellent_ara,text):
            excellent_sayac += 1
            print(match)
            print(excellent_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1

        for match in re.finditer(comfortable_ara,text):
            comfortable_sayac += 1
            print(match)
            print(comfortable_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1
        
        for match in re.finditer(best_ara,text):
            best_sayac += 1
            print(match)
            print(best_sayac)
            print(tum_otel_isimleri[i]) 
            pozitif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_kelime_toplam = pozitif_kelime_toplam + 1
        
        i = i+1   

i = 0
for x in yorumlar :
        
        text = x
        
        not_good_ara = "(?i)not good"   #"(?i)word" case insensitive
        not_good_sayac = 0      
        
        not_clean_ara = "(?i)not clean"
        not_clean_sayac = 0
        
        not_helpfull_ara = "(?i)not helpful*"
        not_helpfull_sayac = 0
        
        unfriendly_sayac = "((?i)unfriendly|(?i)not friendly)"
        unfriendly_sayac_counter = 0
        
        bad_ara = "(?i)bad"
        bad_sayac = 0
        
        uncomfortable_ara = "(?i)uncomfortable"
        uncomfortable_sayac = 0

        for match in re.finditer(not_good_ara,text):  
            not_good_sayac += 1
            good_sayac =good_sayac -1
            print(match)
            print(not_good_sayac)
            print(tum_otel_isimleri[i]) 
            negatif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_yorumlar.remove(tum_otel_isimleri[i])           # not good kelimesini aratırken good kelimesini de buluyor ve 
                                           # pozitif_yorumlar'e  atıyor doğru sonuç çıkması için pozitif_yorumlar ten 1 siliyoruz
            negatif_kelime_toplam = negatif_kelime_toplam + 1   
             
 
            
        for match in re.finditer(not_clean_ara,text):
            not_clean_sayac += 1
            print(match)
            print(not_clean_sayac)
            print(tum_otel_isimleri[i]) 
            negatif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_yorumlar.remove(tum_otel_isimleri[i])
            negatif_kelime_toplam = negatif_kelime_toplam + 1

        for match in re.finditer(not_helpfull_ara,text):
            not_helpfull_sayac += 1
            print(match)
            print(not_helpfull_sayac)
            print(tum_otel_isimleri[i]) 
            negatif_yorumlar.append(tum_otel_isimleri[i])
            pozitif_yorumlar.remove(tum_otel_isimleri[i])
            negatif_kelime_toplam = negatif_kelime_toplam + 1

        for match in re.finditer(unfriendly_sayac,text): #
            unfriendly_sayac_counter += 1
            print(match)
            print(unfriendly_sayac_counter)
            print(tum_otel_isimleri[i]) 
            negatif_yorumlar.append(tum_otel_isimleri[i])
            negatif_kelime_toplam = negatif_kelime_toplam + 1

        for match in re.finditer(bad_ara,text):
            bad_sayac += 1
            print(match)
            print(bad_sayac)
            print(tum_otel_isimleri[i]) 
            negatif_yorumlar.append(tum_otel_isimleri[i])
            negatif_kelime_toplam = negatif_kelime_toplam + 1

        for match in re.finditer(uncomfortable_ara,text):
            uncomfortable_sayac += 1
            print(match)
            print(uncomfortable_sayac)
            print(tum_otel_isimleri[i]) 
            negatif_yorumlar.append(tum_otel_isimleri[i])
            negatif_kelime_toplam = negatif_kelime_toplam + 1
            
            

   
   

        
        i = i+1      


# In[96]:


print("Veri setindeki tüm pozitif kelimelerin toplami = ")    
print(pozitif_kelime_toplam,"\n")
print("Veri setindeki tüm negatif kelimelerin toplami")
print(negatif_kelime_toplam)


# In[97]:


i=0
for x in pozitif_yorumlar:
        print(i)
        print(pozitif_yorumlar[i])
        i = i+1


# In[98]:


from collections import Counter   
import pprint

# pozitif yorumları Counter ile dictionary'e çevrilmiş bir şekilde pozitif_dict değişkenine atadık  
pozitif_dict = Counter(pozitif_yorumlar)    
 

print("POZİTİF KELİME ÇOKLUĞUNA GÖRE OTEL LİSTESİ :\n") # dizideki ilk 20 otel
print("-------------------------------------------------------\n")

i=1
for x, y in pozitif_dict.items(): 
    print(" ",i,"=",x,"pozitif sayılar: ", y)
    i += 1
    if i>20:
        break
    
print("\n\n")
# negatif yorumları Counter ile dictionary'e çevrilmiş bir şekilde negatif_dict değişkenine atadık   
negatif_dict = Counter(negatif_yorumlar)    
      


# dizideki ilk 20 otel
print("NEGATİF KELİME ÇOKLUĞUNA GÖRE OTEL LİSTESİ :\n") 
print("-------------------------------------------------------\n")


i=1
for x, y in negatif_dict.items():
    print(" ",i,"=",x,"negatif sayılar: ", y)
    i += 1
    if i>20:
        break    
        

print("\n\n")

print("POZİTİF VE NEGATİF KELİMELERİN FARKLARININ OTEL LİSTESİ :\n")
print("-------------------------------------------------------\n")



for x in pozitif_dict: # pozitif_dict'in keyleri

    for y in negatif_dict:  #negatif_dict'in keyleri
        
           
        if (x == y):  # pozitif_dict'teki otel  == negatif_dict deki otel
            pozitif_dict[x] = pozitif_dict[x] - negatif_dict[y] 
   



pozitif_dict= collections.Counter(pozitif_dict).most_common(20)                         
pprint.pprint(pozitif_dict)







# In[99]:


import collections  
with open("veri.txt") as f:      # with kullandık txt dosyasını açtırdık
    text = f.read()

kelimeler = re.compile(r"[\w']+", re.U).findall(text)   # re.U == re.UNICODE
collections_sayac = collections.Counter(kelimeler)
print(collections_sayac)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




