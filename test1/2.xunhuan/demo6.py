for i in range(1,5):
    for j in range(1,5):
        if i>=j:     #输出三角形，去掉则为矩形
            print("*",end='\t')  #换行输出，并添加空格
    print()  #不换行