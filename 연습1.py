nums = [15,30,10,20]
print('현재 리스트:', nums)
nums.append(40)
print('append(40)후의 리스트:', nums)
print(nums.pop())
print(nums)
print('pop()후의 리스트 : ', nums)
nums.sort()
print('sort()후의 리스트 : ', nums)
nums.reverse()
print('reverse()후의 리스트 : ', nums)

print('20값의 위치:' ,nums.index(20))

nums.insert(2,222)
print('insert(2,222) 후의 리스트 : ', nums)
nums.remove(222)
print('remove(222)후의 리스트: ', nums)
nums.extend([77,88,77])
print('extend([77,88,77]후의 리스트:' , nums)

print('77값의 개수:',nums.count(77))
