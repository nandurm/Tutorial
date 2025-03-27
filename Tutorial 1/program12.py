def sum_and_average_of_numbers(numbers):
    positive_sum = sum(num for num in numbers if num > 0)
    negative_sum = sum(num for num in numbers if num < 0)
    positive_avg = positive_sum / len([num for num in numbers if num > 0]) if positive_sum > 0 else 0
    negative_avg = negative_sum / len([num for num in numbers if num < 0]) if negative_sum < 0 else 0
    return positive_sum, negative_sum, positive_avg, negative_avg

numbers = [int(input(f"Enter integer {i+1}: ")) for i in range(4)]
positive_sum, negative_sum, positive_avg, negative_avg = sum_and_average_of_numbers(numbers)
print(f"Positive Sum: {positive_sum}, Negative Sum: {negative_sum}, Positive Average: {positive_avg}, Negative Average: {negative_avg}")
