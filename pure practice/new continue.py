numbersTaken=[2,5,12,13,17]
print("here are the jersey numbers still available ")
for x in range(1,20):
    if x in numbersTaken:
        continue
    print(x)