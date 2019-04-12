import fileinput


class solution:
    def ownWay(self, string):
        cal_str = ['S', 'E']
        rev_str = ''
        for i in range(len(string)-1):
            ele_string = string[i]
            if ele_string != cal_str[0]:
                rev_str += cal_str[0]
            else:
                rev_str += cal_str[1]
        return rev_str

def main():
    input_list = []
    for line in fileinput.input():
        input_list.append(line)

    for i in range(len(input_list)):
        if i == 0:
            continue
        elif i % 2 == 0:
            rev_str = solution().ownWay(input_list[i])
            print('Case #{}: {}'.format(int(i / 2), rev_str))


if __name__ == '__main__':
    main()


