from ind_Mel import *
patsiendid=[]
tulemused=[]

patsiendid_D_siseta_andmed(patsiendid,tulemused)





while True:
    v=int(input("1. Составить список пациентов с недостатком витамина D и вывести его на экран\n2. Средний показатель витамина \n3. Отобразить список выбранного кол-ва человек с  самым большим показателем\n4. Осуществить поиск пациентов по имени и вывести на экран его результат\n5. Удалить данные пациента из списка\n6. Выход\n"))
    if v==1:
        
            patsiendid_D_below_30(patsiendid,tulemused)
            
        
            
                

            
    elif v==2:
        
                patsiendid_D_avg(patsiendid,tulemused)
                

    elif v==3:
                patsiendid_D_top(patsiendid,tulemused)
    elif v==4:
                patsiendid_D_find(patsiendid,tulemused)
    elif v==5:
                patsiendid_D_del(patsiendid,tulemused)


    elif v==6:
        break
print(patsiendid)
print(tulemused)


