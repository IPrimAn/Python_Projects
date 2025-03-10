List=[1,0,3,0,5,0,6,0]
count_list=len(List)
Zero_count=List.count(0)

for i in range(Zero_count):
    index=List.index(0)
    Delete_zero=List.pop(index)
    List.append(Delete_zero)
print(List)