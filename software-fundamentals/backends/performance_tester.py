from time import perf_counter, sleep

start = perf_counter()
# sleep(1) # The thing you want to time
stop = perf_counter()

# print(stop - start)

def length_last_word(s: str):
    count = 0
    s = s.rstrip()
    for i in range(len(s), -1, -1):
        if s[i].isspace():
            return count
        count += 1


length_last_word("Hi")
