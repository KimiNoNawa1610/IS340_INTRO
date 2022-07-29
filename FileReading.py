file = open('test.txt', 'r') #create a file   
lines = file.readlines() #read the file   
t=0# assign the initial value
x=[]#assign a list
for line in lines:#condition to write
    square = int(line.rstrip())**2  #calculation  
    print (square)#out put the calculation
    x.append(square)
    file1= open('random.txt', 'w')#open a ramdom file
    file1.write(str(x))#write the ramdom file
    file1.write('\n Nhan\n Deva')#write the name
file1.close()#close file
