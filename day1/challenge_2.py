
import csv
import re
valid_nums = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,'eight':8,'nine':9}

def parse_csv():
    with open('day1.csv', 'r') as f:
        doc = csv.reader(f)
        doc = [line for line in doc]
    return doc



def get_first_and_last_digit(line):
    line = line[0]
    x = [(str(digit), idx) for idx, digit in enumerate(line) if digit.isdigit()]+ find_number_as_str(line)

    y = sorted(x,key = lambda x: x[1])
    print(y)
    s_num = str(y[0][0])
    l_num = str(y[-1][0])
    num = s_num + l_num
    return int(num)
   

def find_number_as_str(s) ->tuple[str,int]:

    all_numbers = []

    for number_word, number_value in valid_nums.items():
        for match in re.finditer(number_word, s):
            start_position = match.start()
            all_numbers.append((int(number_value), start_position))

    all_numbers = sorted(all_numbers, key=lambda x: x[1])
    return all_numbers


if __name__ == '__main__':
    list_of_nums = []
    codes = parse_csv()
    for i,line in enumerate(codes):
        num = get_first_and_last_digit(line)
        list_of_nums.append(num)
    
        
    print(sum(list_of_nums))
    print(get_first_and_last_digit(['eight959tzxkgqjd']))


   
   
 