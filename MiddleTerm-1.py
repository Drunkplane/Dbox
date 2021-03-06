# 从成绩单文件 report.txt 中读取班级成绩，并完成统计分析

# 要求：
# 名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分
# 0 平均 72 67 76 47 63 73 77 73 82 630 70.0
# 1 小S 94 90 96 89 92 84 83 80 82 790 87.8
with open ("report.txt",encoding="utf-8") as f:
    lines=f.readlines()   #   lines是一个list,中的每一个元素就是文本中的一行（一个string)

lst=[]

for line in lines: #每一行都是一个string,可以使用string的方法split,得到一个list
    l=line.split()  #l是list
    A_Guy=[]    #每一行重新定义一个list：A_Guy；让lst中的每一行都是一个人的数据，同时算出他的总分和平均分，加到末尾
    A_Guy_Sum=0
    for i in l:
        try:
            A_Guy.append(int(i))
            A_Guy_Sum+=int(i)
        except:
            A_Guy.append(i)
    A_Guy.append(A_Guy_Sum)
    A_Guy.append(round(A_Guy_Sum/9,1))
    lst.append(A_Guy)

#print(lst)

lst.sort(key=lambda x:x[-1],reverse=1)  #排序，表头变到最后一个
lst.insert(0,lst[-1]); del lst[-1]  #把最后一个放到第一个
#print(lst)

lst_avg=["平均"]
for ii in range(1,12):
    subject = 0  # 每一科的总分
    for j in lst[1:]:
        subject+=j[ii]
    lst_avg.append(round(subject/(len(lst)-1),1))
    #print(lst_avg)

lst.insert(1,lst_avg)
#print(lst)

for i in lst:
    if lst.index(i)==0:
        i.insert(0,"名次")
    else:
        i.insert(0,lst.index(i)-1)
lst[0][-1]="平均分"; lst[0][-2]="总分"
#print(lst)

with open('result.txt','w',encoding='utf8') as f:
    for i in lst[0]:    #写第一行
        f.write(str(i)+" ")
    f.write("\n")

    for lines_sec in lst[1:]:   #写剩下的，并把60分以下的换成“不及格”
        f.write(str(lines_sec[0])+" ")
        f.write(str(lines_sec[1])+" ")
        for i in lines_sec[2:]:
            if int(i)<60:
                i="不及格"
            f.write(str(i)+" ")
        f.write('\n')