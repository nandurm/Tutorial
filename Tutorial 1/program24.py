def numbers_with_digit_sum_divisible_by_9():
    return [num for num in range( 100, 1001) if sum(int(digit) for digit in str(num)) % 9 == 0]

print(numbers_with_digit_sum_divisible_by_9())

