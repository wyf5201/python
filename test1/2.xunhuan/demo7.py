for i in range(1,10):      #行
    for j in range(1,i+1):    #列
        print(i,"*",j,"=",i*j,end='\t')  #换行输出，并添加空格
    print()  #不换行