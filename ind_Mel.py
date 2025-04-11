from statistics import *
from random import *
def patsiendid_D(nimed:list,D:list)->list:
    """Составляет или дополняет  список пациентов и их результатов анализов на витамин D
    :nimed:list: Список имён
    :D:list: Список результатов анализов
    
    """
try:
    while True:
        c=int(input("Количество пациентов, вводимое в список: "))
        
        if c>0:
            break
        else:
            print("Количество должно быть положительным")
    nimed=[]
    D=[]
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
    while True:
        v=int(input("1. Составить список пациентов с недостатком витамина D и вывести его на экран\n2. Средний показатель витамина \n3. Отобразить список выбранного кол-ва человек с  самым большим показателем\n4. Осуществить поиск пациентов по имени и вывести на экран его результат\n5. Выход\n"))
        if v==1:
            print(D)
            tulemus=False
            for i in range(c):
               if D[i]<30:
                   
                   
                   print(nimed[i])
                   print(D[i])
                   tulemus=True
            if tulemus==False:
                print("Количество D витамна в крови пациентов в норме!")

            
        elif v==2:
            D_avg= mean(D)
            print(f"Средний показатель витамина D {D_avg}")
        elif v==3:
            print(3)
        elif v==4:
            name=input("Имя пациента:  ")
            leitud=False
            for j in range(c):
              if nimed[j]==name:
                print(f"{name} содержание витамина D: {D[j]}")
                leitud=True
            if leitud==False:
                print("Данных нет")
        elif v==5:
            break

       
        print(D)
        print(nimed)
except Exception as e:
         print ("Viga:",e)




