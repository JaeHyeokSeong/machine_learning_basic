print("8-6 퀴즈\n")

for day in range(1, 51):
    file_name = str(day) + "주차.txt"
    with open(file_name, "w", encoding="utf8") as file:
        file.write(f"- {day} 주차 주간보고 -\n")
        file.write("부서 :\n")
        file.write("이름 :\n")
        file.write("업무 요약 :\n")
