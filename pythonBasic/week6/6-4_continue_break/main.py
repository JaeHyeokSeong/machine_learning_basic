print("continue 그리고 break practise")

absentStudent = [2, 7]
noBook = [9]

for student in range(1, 11):
    if student in absentStudent:
        print(f"{student} 학생 결석")
        continue
    elif student in noBook:
        print(f"{student} 책 없음, 수업 종료")
        break
    print(f"{student} 학생 책을 읽어 주세요")
