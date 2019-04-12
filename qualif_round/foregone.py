import fileinput


class solution:
    def getDigital(self, N: int):
        rev_k = 0
        while True:
            if 10 ** (rev_k + 1) > N >= 10 ** rev_k:
                return rev_k
            else:
                rev_k += 1
        return rev_k

    def foregone(self, N: int):
        if N == 7 or N == 8 or N == 9:
            return N - 2, 2
        elif N <= 10:
            return int(N / 2), N - int(N / 2)

        num_N = self.getDigital(N)

        B_val = 0
        N_ori = N
        dig_list = []
        flag = False
        for i in reversed(range(num_N + 1)):
            dig_val = int(N / (10 ** i))
            dig_list.append(dig_val)
            if dig_val == 4:
                B_val += 2 * (10 ** i)
                pas_val = dig_val * (10 ** i)
                N -= pas_val
                flag = True
            else:
                pas_val = dig_val * (10 ** i)
                N -= pas_val

        if not flag:
            B_val = dig_list[0] * (10 ** num_N)
            if N_ori == B_val and dig_list[0] not in [8, 9]:
                return int(N_ori / 2), int(N_ori / 2)
            elif N_ori == B_val and dig_list[0] in [8, 9]:
                return 3 * (10 ** num_N), (dig_list[0] - 3) * (10 ** num_N)

        A_val = N_ori - B_val

        return A_val, B_val


def main():
    so = solution()
    input_list = []
    for line in fileinput.input():
        input_list.append(int(line))

    for i in range(len(input_list)):
        if i == 0:
            continue
        else:
            rev_A = so.foregone(input_list[i])[0]
            rev_B = so.foregone(input_list[i])[1]
            print("Case #{}: {} {}".format(i, rev_A, rev_B))


if __name__ == '__main__':
    main()

