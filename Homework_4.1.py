List=[]
count_list=len(List)
Zero_count=List.count(0)

for i in range(Zero_count):
    index=List.index(0)
    Delete_Zero=List.pop(index)
    List.append(Delete_Zero)
print(List)