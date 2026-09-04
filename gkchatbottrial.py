with open ("data1.txt","r") as file:
    data=file.readlines()
    line=[line.strip() for line in data]
    #print (line)
with open ("data2.txt","r") as file2:
    data2=file2.readlines()
    line2=[line2.strip() for line2 in data2]
    #print(line2)
dic= dict(zip(line,line2))
def misspelled(i):
    stopwords = {"what", "is", "the", "of", "who", "are", "a", "an", "in", "you", "your", "how", "to", "do", "i", "can", "does", "for", "and", "be", "was", "were", "on", "as"}
    score =[]
    question=[]
    for n in dic.keys():
        word_i=set(i.lower().split())
        word_n=set(n.lower().split())
        t={o for o in word_i if o not in stopwords}
        f={u for u in word_n if u not in stopwords}
        count= len(f & t)
        score.append(count)
        question.append(n)
    
    highest=max(score )
    if highest >0:
        index= score.index(highest)
        leg=question[index]
        return leg
while True:
    import string
    i= input().lower()
    i=i.translate(str.maketrans("","",string.punctuation))
    if i=="bye":
        print("see you soon")
        break
    elif i=="hi":
        print("Hi How Can i help you")
    elif i=="hello":
        print("yes how can i help you ")
    elif misspelled(i)!=None :
        print(dic[misspelled(i)])
    else :
        print("what are you trying to tell")
        
    
