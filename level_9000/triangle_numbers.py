# Triangle Numbers
STOP = 100
start_num = 0


while start_num < STOP :
    triangle_nums = start_num * (start_num + 1) // 2
    start_num += 1
    print(triangle_nums)