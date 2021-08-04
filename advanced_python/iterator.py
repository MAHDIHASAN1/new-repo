# Iterators 
# Iterable
# Iterable string, list, tuple, set, dictionary

nums = [12, 34, 56, 78]   # iterable

my_iterator = iter(nums)  # iterator

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))            


name = "mahdi hasan"

name_iterator = iter(name)

print(next(name_iterator))
print(next(name_iterator))
print(next(name_iterator))
print(next(name_iterator))
print(next(name_iterator))
 
for item in name_iterator :
    print(item)

# __iter__, __next__, 
# __ = duble underscore / dunder methods

class PowerTwo:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        result = self.num ** 2
        self.num += 1
        return result

my_num = PowerTwo()
num_iterator = iter(my_num)

print(next(num_iterator))
print(next(num_iterator))
print(next(num_iterator))
print(next(num_iterator))





class powerTwo_1:
    def __iter__(self_1):
        self_1.num_1 = 1
        return self_1

    def __next__(self_1):
        if self_1.num_1 <= 3:
            result_1 = self_1.num_1 ** 2
            self_1.num_1 += 1
        
        else:
            raise StopIteration

        return result_1

my_num_1 = powerTwo_1()
num_iterator_1 = iter(my_num_1)

print(next(num_iterator_1))
print(next(num_iterator_1))
print(next(num_iterator_1))
# print(next(num_iterator_1))

#for number in num_iterator_1:
#    print("Num:",number)






















































