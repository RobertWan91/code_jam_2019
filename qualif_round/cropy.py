import fileinput


class Solution:
    def breaknum(self, nums):
        end_num = int(nums**0.5)
        for i in range(2, end_num+1):
            if nums%i == 0:
                return i, int(nums/i)
        return []

    def decipherMin(self, nums_list):
        # scan and find the minimal to start
        # [value, index]
        rev_list = [float('inf'), 0]
        len_nums = len(nums_list)
        for i in range(1, len_nums-1):
            if nums_list[i] != nums_list[i-1] and nums_list[i] != nums_list[i+1]:
                if nums_list[i] < rev_list[0]:
                    rev_list[0] = nums_list[i]
                    rev_list[1] = i

        if nums_list[0] != nums_list[1] and nums_list[0] < rev_list[0]:
            rev_list[0] = nums_list[0]
            rev_list[1] = 0

        if nums_list[-1] != nums_list[-2] and nums_list[-1] < rev_list[0]:
            rev_list[0] = nums_list[-1]
            rev_list[-1] = len_nums-1
        return rev_list

    def decipher_list(self, start, end, nums_list):
        if start == end:
            factor_A, factor_B = self.breaknum(nums_list[start:end+1][0])
            return [factor_A, factor_B]
        if start < end:
            start_i, end_i = start, end

        # j: L+1: nums[j]: nums[L]
            list_tuple = []
            tag = 0
            for i in range(start_i, end_i+1):
                if i == start_i:
                    factor_i1, factor_i2 = self.breaknum(nums_list[i])
                    list_tuple.append([factor_i1, factor_i2])
                    tag += 1
                    continue
                if tag == 1:
                    previous_factor = list_tuple[-1].copy()
                    if nums_list[i] % previous_factor[0] == 0:
                        list_tuple.append([previous_factor[0], int(nums_list[i]/previous_factor[0])])
                        list_tuple[0][1] = previous_factor[0]
                        list_tuple[0][0] = previous_factor[1]
                    else:
                        list_tuple.append([previous_factor[1], int(nums_list[i]/previous_factor[1])])
                    tag += 1
                else:
                    if nums_list[i] == nums_list[i-1]:
                        list_tuple.append(list_tuple[-1][::-1])
                        tag += 1
                    else:
                        previous_factor = list_tuple[-1]
                        assert nums_list[i] % previous_factor[1] == 0
                        list_tuple.append([previous_factor[1], int(nums_list[i]/previous_factor[1])])
                        tag += 1
            rev_list = [item[0] for item in list_tuple]
            rev_list.append(list_tuple[-1][-1])
            return rev_list[1:]

        elif start > end:
            start_i, end_i = end, start
            list_tuple = []
            tag = 0
            for i in reversed(range(start_i, end_i+1)):
                # print(nums_list[i])
                # print(list_tuple)
                if i == end_i:
                    factor_i1, factor_i2 = self.breaknum(nums_list[i])
                    list_tuple.append([factor_i1, factor_i2])
                    tag += 1
                    continue
                if tag == 1:
                    previous_factor = list_tuple[-1].copy()
                    if nums_list[i] % previous_factor[0] == 0:
                        list_tuple.append([previous_factor[0], int(nums_list[i]/previous_factor[0])])
                        list_tuple[0][1] = previous_factor[0]
                        list_tuple[0][0] = previous_factor[1]

                    else:
                        list_tuple.append([previous_factor[1], int(nums_list[i]/previous_factor[1])])
                    tag += 1
                else:
                    if nums_list[i] == nums_list[i+1]:
                        list_tuple.append(list_tuple[-1][::-1])
                        tag += 1
                    else:
                        previous_factor = list_tuple[-1]
                        assert nums_list[i] % previous_factor[1] == 0
                        list_tuple.append([previous_factor[1], int(nums_list[i]/previous_factor[1])])
                        tag += 1
            rev_list = [item[0] for item in list_tuple[1:]]
            rev_list.append(list_tuple[-1][-1])
            return list(reversed(rev_list))

    def convert(self, list_nums):
        dict_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        list_uniq = list(set(list_nums))
        list_uniq.sort()
        assert len(list_uniq) == 26
        rev_dict = {}
        for i in range(len(dict_let)):
            rev_dict[str(list_uniq[i])] = dict_let[i]

        return rev_dict

    def decipher(self, N, L, nums_list):
        mid_list = self.decipherMin(nums_list)
        mid_index = mid_list[1]
        if mid_index == 0:
            list_rev1 = self.decipher_list(mid_index, 0, nums_list)
            list_rev2 = self.decipher_list(mid_index, L-1, nums_list)
            if list_rev1[0] == list_rev2[0]:
                new_list = [list_rev1[1]]
                new_list.extend(list_rev2)
            else:
                new_list = [list_rev1[0]]
                new_list.extend(list_rev2)
        elif mid_index == L-1:
            list_rev1 = self.decipher_list(mid_index, 0, nums_list)
            list_rev2 = self.decipher_list(mid_index, L-1, nums_list)
            if list_rev2[0] == list_rev1[-1]:
                # new_list = [list_rev2[1]]
                new_list = list_rev1
                new_list.extend([list_rev2[1]])
            else:
                new_list = list_rev1
                new_list.extend([list_rev2[0]])
        else:
            list_rev1 = self.decipher_list(mid_index, 0, nums_list)
            list_rev2 = self.decipher_list(mid_index, L-1, nums_list)
            new_list = list_rev1
            new_list.extend(list_rev2)

        # print('generated list: ', new_list)
        dict_ref = self.convert(new_list)
        # final
        rev_str = ''
        for num_element in new_list:
            rev_str += dict_ref[str(num_element)]

        return rev_str


def main():
    input_list = []
    for line in fileinput.input():
        input_list.append(line)
    i = 0
    len_input = int(input_list[0])
    while i <= 2 * len_input:
        if i == 0:
            i += 1
            continue
        else:
            nums = input_list[i].split(' ')
            n = int(nums[0])
            l = int(nums[1])
            nums_list = input_list[i+1].split(' ')
            # print(nums_list)
            new_nums_list = []
            for element in nums_list:
                try:
                    new_nums_list.append(int(element))
                except ValueError:
                    continue
            rev_string = Solution().decipher(n, l, new_nums_list)
            print("Case: #{}: {}".format(int((i + 1) / 2), rev_string))
            i += 2


if __name__ == "__main__":
    main()

