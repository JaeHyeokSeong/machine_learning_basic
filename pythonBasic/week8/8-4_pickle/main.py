import pickle

print("8-4 pickle practise\n")

customer = {"son": "soccer", "lee": ["soccer", "fifa", "2001"]}
info = customer["lee"]
# print(info)

profile = open("profile.pickle", "wb")
pickle.dump(info, profile)
profile.close()

with open("profile.pickle", "rb") as profile:
    print(f"contents : {pickle.load(profile)}")
