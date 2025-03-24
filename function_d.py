def max_value(numbers):
<<<<<<< HEAD
    if not numbers:
        return None
    
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num
=======
    return max(numbers)
>>>>>>> d3aa7dca42b9a1a06ef54f9074d48a5b0e8f483f


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
