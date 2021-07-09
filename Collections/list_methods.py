nums = [1,  2, 7, 8,  3,  4,  5]
print(len(nums))

print(len([57,68,91,20]))


nums[2] = 17
print("nums_ch:",nums)


print(min(nums))

print(max(nums))


print("nums_sum:",sum(nums))
print("nums_sum1:",sum(nums[:4]))

nums.reverse()
print("nums_re:",nums)


nums.sort()
print("nums_so:",nums)


print(dir(nums))


nums.append(100)
print(nums)


print(nums.insert(2, 2.5))

nums.insert(4,3.5)
print("nums_insert:",nums)


nums.remove(2)
print("nums_rm1:",nums)


#del nums[2:5]
#print("nums_del:",nums)

#del nums[2]
#print("nums_del:",nums)

#del nums[2:]
#print("nums_del1:",nums)


#print(nums.pop())

#nums.pop()
#print(nums)


#nums.clear()
#print(nums)


nums.append("mahdi hasan")   
print(nums)


nums_cp = nums.copy()
nums_cp.append("tahmida")
print("nums_cp:",nums_cp)


name = [22,56,22,54,]
print("name_count:",name.count(22))


name.extend(nums_cp)
print("name:",name)

name = name + nums_cp
print("name:",name)

name1 = name + nums_cp
print("name1:",name1)


print(name.index(22))
















