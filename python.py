def calculation_square(number: int) -> int:
    return number*number
    

if __name__ == '__main__':
    input_number: int = int(input())
    square_number: int = calculation_square(input_number)
    print(square_number)
   