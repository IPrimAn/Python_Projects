List=[0,2,2]

SUM=0

for i in range(0, len(List), 2):
    SUM=SUM+List[i]

result=SUM*List[-1]
print(result)
