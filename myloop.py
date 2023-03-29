


#creating a list of numbers. 20 numbers
ls1 = range(1,20)
ls1 = list(ls1)
print(ls1)
# Loop through the values 
for i in ls1:
    print("i is ",i)
# practical example. in the list of cities below change ksm to kisumu
mydata=["Nrb","Msa","ksm","Eld",'Nkr']
maydataindexes = list(range(0,len(mydata)))
print(maydataindexes)
for i in [0,1,2,3,4]:
    if mydata[i] == "Ksm":
        mydata[i] = "Kisumu"
        #Break will stop the loop
        break
    else:
        pass
print(mydata)
#Loops are used to get daat from a database/table and display
