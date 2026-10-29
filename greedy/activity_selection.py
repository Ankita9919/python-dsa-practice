
n = int(input("Enter number of activities: "))
activities = []

for i in range(n):
    start, finish = map(int, input().split())
    activities.append((start, finish))

activities.sort(key=lambda x: x[1])

count = 0
last_finish = 0

for start, finish in activities:
    if start >= last_finish:
        print(start, finish)
        count += 1
        last_finish = finish

print("Maximum activities:", count)
