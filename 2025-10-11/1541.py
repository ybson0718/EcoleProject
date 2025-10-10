#잃어버린 괄호

expression = input()

parts = expression.split('-')

first_part_nums = parts[0].split('+')
answer = 0
for num_str in first_part_nums:
    answer += int(num_str)

for i in range(1, len(parts)):
    other_part = parts[i]

    other_part_nums = other_part.split('+')
    sum_to_subtract = 0
    for num_str in other_part_nums:
        sum_to_subtract += int(num_str)

    answer -= sum_to_subtract
print(answer)