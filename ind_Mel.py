

from statistics import *
from random import *

def patsiendid_D_siseta_andmed(nimed:list,D:list,)->list:
    """Составляет или дополняет  список пациентов и их результатов анализов на витамин D
    :nimed:list: Список имён
    :D:list: Список результатов анализов
    :c:int: Количество пациентов вводимое в список
    
    """
    try:
        
        while True:
            c=int(input("Количество пациентов, вводимое в список: "))
        
            if c>0:
                break
            else:
                print("Количество должно быть положительным")
        
        for l in range(c):
            while True:
                n=input("Имя:")
                if n.isalpha():

                    nimed.append(n)
                    break
                else:
                    print("Пиши имя словами")
            
            a=randint(1,100)
            D.append(a)
        return D,nimed,c
            
    except Exception as e:
            print ("Viga:",e)

def patsiendid_D_below_30(nimed:list,D:list)->list:
    """Составляет список пациентов с недостатком витамина D
    :nimed:list: Список имён
    :D:list: Список результатов анализов
    
    """

    
           
            
            
    tulemus=False
    for i in range(len(nimed)):
                   if D[i]<30:
                   
                   
                       print(nimed[i])
                       print(D[i])
                       tulemus=True
                   
    if tulemus==False:
                    print("Количество D витамна в крови пациентов в норме!")
                    
    
def patsiendid_D_avg(nimed:list,D:list)->list:
    """Выдаёт средний показатель витамина D
    :nimed:list: Список имён
    :D:list: Список результатов анализов
    """

    D_avg= mean(D)
    print(f"Средний показатель витамина D {D_avg}")       
            
        

def patsiendid_D_top(nimed:list,D:list)->list:
    """Составляет топ Т пациентов с наилучшими показателями витамина D
    :nimed:list: Список имён
    :D:list: Список результатов анализов
    
    """

            
    T=int(input("Сколько пациентов с наилучшими показателями хотите видеть?: "))
    if T>0:
             
             
                     
                     pal=D.copy()
                     pal.sort(reverse=True)
                     nam=[]
                     for l in range(T):
                
                        ind=D.index(pal[l])

                        nam.append(nimed[ind])
                        
 
                     print("Лучшие")
                     for x in range(T):

                            print(f"{nam[x]} - {pal[x]}")
                     
    else:
                        print("Напиши число")
def patsiendid_D_find(nimed:list,D:list)->list:
    """Осуществляет поиск по имени пациента
    :nimed:list: Список имён
    :D:list: Список результатов анализов
    
    """
    name=input("Имя пациента:  ")
    leitud=False
    for j in range(len(nimed)):
                  if nimed[j]==name:
                    print(f"{name} содержание витамина D: {D[j]}")
                    leitud=True

                    
                  if leitud==False:
                    print("Данных нет")
def patsiendid_D_del(nimed:list,D:list)->list:
    """Удалить пациента из списка
    :nimed:list: Список имён
    :D:list: Список результатов анализов
    
    """
    name=input("Введи имя пациента, которого необходимо удалить: ")
    
    if name.isalpha():
                    k=nimed.count(name)
                    if k>0:
                        for j in range(k):

                            ind=nimed.index(name)
                            D.pop(ind)
                            nimed.remove(name)
                        return D,nimed
                        
                        
                    else:
                        print("Данные отсутствуют")
        


            
            

        
    # except Exception as e:
    #         print ("Viga:",e)




