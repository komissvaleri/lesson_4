
isch_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [num for i, num in enumerate(isch_list) if i > 0 and isch_list[i] > isch_list[i - 1]]

print(res_list)

