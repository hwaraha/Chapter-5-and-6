# LAB 5-1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: (x % 2 == 0), list1))
print("Even numbers in the list: ", even_list)

for num in range(2, 11, 2):
    print(num)

nations = ['Korea', 'China', 'India', 'Nepal']
print("nations =", nations)

friends = ['Lina', 'Ana', 'Mina']
print("friends =", friends)

str_ = ['X', 'Y', 'Z']
print("string =", str_)

# LAB 5-2
prime_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(prime_list[0])
print(prime_list[5])
print(prime_list[-4])

nations = ['Korea', 'China', 'Russia', 'Malaysia']
print(nations[0])
print(nations[-1])
print(nations[len(nations)-1])

# LAB 5-3
prime_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("List of decimals: ", end = '')
print(*prime_list, sep = ", ")

prime_list.append(11)

print("List of decimals after appending: ", end = '')
print(*prime_list, sep = ", ")

# LAB 5-4
prime_list = [2, 3, 5, 7]
print(min(prime_list))
print(max(prime_list))
print(sum(prime_list))
print(len(prime_list))

nations = ["Korea", "China", "Russia", "Malaysia"]
print(min(nations))
print(max(nations))

# LAB 5-5
a = [1, 2, 3]
b = [10, 20, 30]
a.append(b)
print(a)

a = [1, 2, 3]
b = [10, 20, 30]
a.extend(b)
print(a)

nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nlist.insert(0, 0)
print(nlist)
nlist.reverse()
print(nlist)
nlist.pop()
print(nlist)

# LAB 5-6
list1 = [1, 2, 3]
print(list1 *3)
print(list1 *4)

# LAB 5-7
nlist = range(15)
print(list(nlist))

n_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
s_list1 = n_list[:5]
print(s_list1)
s_list2 = n_list[5:11]
print(s_list2)
s_list3 = n_list[11:15]
print(s_list3)
s_list4= n_list[2:11:2]
print(s_list4)
s_list5 = n_list[10:5:-1]
print(s_list5)
s_list61 = n_list[10::-1]
print(s_list61)
s_list6 = s_list61[:10:2]
print(s_list6)

# LAB 6-1
capital_dic = {'Korea': 'Seoul', 'China': 'Beijing', 'USA': 'Washington DC'}
print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic['USA'])

fruits_dic = {'apple': 5000, 'banana': 4000, 'grape': 5300, 'melon': 6500}
print('apple costs', fruits_dic['apple'], 'won')
print('banana costs', fruits_dic['banana'], 'won')
print('grape costs', fruits_dic['grape'], 'won')
print('melon costs', fruits_dic['melon'], 'won')

# LAB 6-2
person = {'Name': 'Hong Gil Dong', 'age': 26, 'weight': 82}
person['hobby'] = 'soccer'
print(person)
person['father'] = 'Hong Pan Sul'
print(person)
del person['age']
print(person)

# LAB 6-3
capital_dic = {'Korea': 'Seoul', 'China': 'Beijing', 'USA': 'Washington DC'}
print('Korea' in capital_dic)
print('China' in capital_dic)
print('Indonesia' in capital_dic)
print('Beijing' in capital_dic)

# LAB 6-4
fruits_dic = {'apple': 6000, 'melon': 3000, 'banana': 5000, 'orange': 7000}
fruits_dic.keys()
fruits_dic.values()
fruits_dic.pop('apple', 6000)
fruits_dic.clear()

# LAB 6-5
fruits_dic = {'apple': 6000, 'melon': 3000, 'banana': 5000, 'orange': 7000}
fruits_list = list(fruits_dic.keys())
print(fruits_list)
fruits_val = list(fruits_dic.values())
print(fruits_val)
fruits_len = len(fruits_dic)
print(fruits_len)
if 'apple' in fruits_dic:
    print('apple is in fruits_dic')

# LAB 6-6
the_day = (1919, 3, 1)
print(the_day[0], 'year', the_day[1], 'month', the_day[2], 'day is current day today' )

a = 30
b = 20
c = 10

# LAB 6-9
lst = ['apple', 'mango', 'banana']
s1 = set(lst)
print(s1)

greet = 'Good afternoon'
s2 = set(greet)
print(s2)

# LAB 6-10
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60, 70}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))






