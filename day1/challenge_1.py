import csv
def parse_csv():
    with open('day1.csv', 'r') as f:
        doc = csv.reader(f)
        doc = [line for line in doc]
    return doc

if __name__ == '__main__':
    list_of_numbs=[]
    doc = parse_csv()
    for line in doc:
        line= line[0]
        all_numbs = [str(digit) for digit in line if digit.isdigit() ]
        s_num = all_numbs[0]
        l_num = all_numbs[-1]
        list_of_numbs.append(int(s_num+l_num))
    print(sum(list_of_numbs))
