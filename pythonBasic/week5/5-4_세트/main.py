print("set - 집합")

visited = {1, 2, 3}
print(type(visited))

visited.add(1)

print(visited)

print(1 in visited)

print(4 in visited)

visited.remove(2)
print(visited)

visited.add(10)
print(visited)

cpp = {"jae", "aljonn", "nick", "oddo"}
python = set(["jae", "nick"])
python.add("oddo")

print(cpp)
print(python)

print(cpp & python)
