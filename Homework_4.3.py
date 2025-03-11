import random

List=[random.randint(1,9) for i in range(random.randint(3, 10))]
print(List)

new_list=List[0:3:2]
new_list_part2=[List[-2]]
new_list.extend(new_list_part2)
print(new_list)
