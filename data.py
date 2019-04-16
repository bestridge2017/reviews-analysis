data = []
count = 0

with open('reviews.txt','r') as f:
    for line in f:
        data.append(line.strip())
        count += 1
        if count % 100000 == 0:
            print(len(data))
print('档案读取完成，总共有',len(data),'笔资料')

sum_len = 0
for d in data:
	sum_len = sum_len +len(d)
print('平均长度是',sum_len/len(data))


new = []

for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'笔留言长度小于100')
print(new[0])
print(new[1])



