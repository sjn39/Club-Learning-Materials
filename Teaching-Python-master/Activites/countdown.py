import time

count = int(input("Enter the number of seconds to count down: "))

while(count > 0):
    print(count)
    count -= 1
    time.sleep(1)