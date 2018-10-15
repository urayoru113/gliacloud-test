urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
    ]

file_ = []
isexist = False
for url in urls:
    isexist = False
    filename = url.rsplit('/', 1)[-1]
    for index, f in enumerate(file_):
        if filename == f[0]:
            file_[index][1] += 1
            isexist = True
    if not isexist:
        file_.append([filename, 1])

file_ = sorted(file_, key=lambda x:x[1], reverse=True)

for i in range(3):
    print(file_[i][0], file_[i][1])
