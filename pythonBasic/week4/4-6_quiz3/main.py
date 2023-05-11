
url = "http://youtube.com"
url = url.replace("http://", "")
url = url[:url.find(".")]
password = url[:3] + str(len(url)) + str(url.count("e")) + "!"

print(password)
