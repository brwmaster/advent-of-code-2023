def main():
    text = get_input_text()
    sum_of_calibration = get_sum_of_calibration(text)
   
    print(sum_of_calibration)

def get_input_text():
    with open("input.txt") as f:
        return f.read()
    

def get_sum_of_calibration(text):
    words = text.split()
    calibration_list = []

    for word in words:
        nums = ""
        for char in word:
            if char.isdigit():
                nums += char

        num = nums[0] + nums[-1]
        calibration_list.append(num)

    return sum(list(map(int, calibration_list)))

  

        


main()