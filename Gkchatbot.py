with open ("data1.txt","r") as file:
    data=file.readlines()
    line=[line.strip() for line in data]
    #print (line)
with open ("data2.txt","r") as file2:
    data2=file2.readlines()
    line2=[line2.strip() for line2 in data2]
    #print(line2)
dic= dict(zip(line,line2))
#print (dic)
while True:
    import string
    i= input().lower()
    i=i.translate(str.maketrans("","",string.punctuation))
    if i=="bye":
        print("see you soon")
        break
    elif i in dic.keys():
        print(dic[i])
    else :
        print("what are you trying to tell")
        
    
