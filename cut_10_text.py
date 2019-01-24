#coding:utf-8



with open('stopwords.txt','r',encoding='utf-8') as f:
    stopword=f.readlines()
    for i in range(len(stopword)):
        stopword[i]=stopword[i][:-1]
    print(stopword)
    with open('final_0.txt', 'r', encoding='utf-8') as f2:
        temp = f2.readlines()
        # print(temp)
        with open('final_0_2.txt', 'w', encoding='utf-8') as f1:
            for perline in temp:
                perword=perline.split()
                for i in perword:
                    if i not in stopword:
                        # print(i)
                        f1.write(i+' ')
                        # a=input()
                f1.write('\n')


with open('stopwords.txt','r',encoding='utf-8') as f:
    stopword=f.readlines()
    for i in range(len(stopword)):
        stopword[i]=stopword[i][:-1]
    print(stopword)
    with open('final_1.txt', 'r', encoding='utf-8') as f2:
        temp = f2.readlines()
        # print(temp)
        with open('final_1_2.txt', 'w', encoding='utf-8') as f1:
            for perline in temp:
                perword=perline.split()
                for i in perword:
                    if i not in stopword:
                        # print(i)
                        f1.write(i+' ')
                        # a=input()
                f1.write('\n')


with open('stopwords.txt','r',encoding='utf-8') as f:
    stopword=f.readlines()
    for i in range(len(stopword)):
        stopword[i]=stopword[i][:-1]
    print(stopword)
    with open('final_2.txt', 'r', encoding='utf-8') as f2:
        temp = f2.readlines()
        # print(temp)
        with open('final_2_2.txt', 'w', encoding='utf-8') as f1:
            for perline in temp:
                perword=perline.split()
                for i in perword:
                    if i not in stopword:
                        # print(i)
                        f1.write(i+' ')
                        # a=input()
                f1.write('\n')