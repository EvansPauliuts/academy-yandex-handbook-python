list_num = []

while True:
    input_num = float(input())

    if input_num > 0:
        if input_num >= 500:
            discount_num = input_num - ((10 * input_num) / 100)
            list_num.append(discount_num)
        else:
            list_num.append(input_num)
    else:
        break


print(sum(list_num))
