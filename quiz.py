filename=open("Crime.csv","r")
print(filename)
i=0
j=0
for line in filename.split('\n'):
    data = line.split(',')
    if data == "Assault"
        i+=data
    if data =="Robbery"
        j+=data
print ("Assault",i,end" ")
print ("Robbery",j,end" ")
