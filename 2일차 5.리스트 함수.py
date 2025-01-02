my_list = [1,2,3,4,5,6,7,8,9]
print("현재 리스트 : %s" %my_list)

my_list.append(10)
print("append(10)을 추가 후 리스트 : %s" %my_list)

print("pop()으로 추출한 값 : %s" %my_list.pop())
print("pop() 후의 리스트 %s" %my_list)

my_list.sort()
print("Sort() 후의 리스트 %s" %my_list)

my_list.reverse()
print("reverse() 후의 리스트 %s" %my_list)

my_list.insert(2,100)
print("insert()로 삽입 후의 리스트 %s" %my_list)

my_list.remove(100)
print("remove()로 삭제 후의 리스트 %s" %my_list)

my_list.extend([100,200,300])
print("extend()로 추가 후의 리스트 %s" %my_list)

print("100의 값의 개수는 %d" %my_list.count(100))