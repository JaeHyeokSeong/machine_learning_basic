from house import House

print("9-12 quiz\n")

houses = [House("강남", "아파트", "매매", "10억", "2010년"), House("마포", "오피스텔", "전세", "5억", "2007년"), House("송파", "빌라", "월세", "500/50", "2000년")]

print(f"총 {len(houses)}의 매물이 있습니다.")
for house in houses:
    house.show_detail()
