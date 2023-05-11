subway = [10, 20, 30]

print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("유재석"))

subway.append("정준하")
print(subway)

subway.insert(1, "노홍철")

print(subway)

subway.insert(4, "정형돈")

print(subway)


val = subway.pop()
print(subway)
print(val)

val = subway.pop()
print(subway)
print(val)

subway.remove("조세호")
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

numbers = [1, 3, 5, 2, 6, 4, 8, 7, 10, 9]
print(numbers)

# ascending
numbers.sort()
print(numbers)

# descending
numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

# numbers.clear()
# print(numbers)

mix_list = ["jae", 23, True]
print(mix_list)

# numbers = [1, 2, 3]
numbers.extend(mix_list)
print(numbers)

major = "computer science"
numbers.append(major)
print(numbers)

numbers.extend(major)
print(numbers)
