import time
def writeInfo():
    date  = time.asctime()
    with open(r'C:\info.txt' ,'a' ,encoding='utf-8') as f:
        f.write(date)


writeInfo()