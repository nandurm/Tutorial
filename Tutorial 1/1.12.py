def sum_and_average(numbers):
    pos_sum = 0  
    neg_sum = 0  
    pos_count = 0  
    neg_count = 0 

    for num in numbers:
        if num > 0:
            pos_sum += num
            pos_count += 1
        elif num < 0:
            neg_sum += num
            neg_count += 1

   
    pos_avg = pos_sum / pos_count if pos_count > 0 else 0
    neg_avg = neg_sum / neg_count if neg_count > 0 else 0

    return pos_sum, pos_avg, neg_sum, neg_avg


nums = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)


pos_sum, pos_avg, neg_sum, neg_avg = sum_and_average(nums)


print(f"Sum of positive numbers: {pos_sum}")
print(f"Average of positive numbers: {pos_avg:.2f}")
print(f"Sum of negative numbers: {neg_sum}")
print(f"Average of negative numbers: {neg_avg:.2f}")
