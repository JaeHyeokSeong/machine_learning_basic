print("6-5 practise")

num = [i for i in range(1, 5)]
print(num)

# 학생들의 각 이름들의 길이를 리스트에 저장하기
student = ["son", "hwan", "kim", "lee"]
student_length = [len(i) for i in student]

print(student_length)

# 학생들의 이름을 대문자로 바꾸기
student_upperCase = [i.upper() for i in student]
print(student_upperCase)
