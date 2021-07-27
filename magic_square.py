"""
We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range .

Example

$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

The matrix looks like this:

5 3 4
1 5 8
6 4 2
We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2
This took three replacements at a cost of |5-8|+|8-9|+|4-7|.

Function Description

Complete the formingMagicSquare function in the editor below.

formingMagicSquare has the following parameter(s):

int s[3][3]: a 3X3  array of integers
Returns

int: the minimal total cost of converting the input square to a magic square
Input Format

Each of the  lines contains three space-separated integers of row s[i].

Constraints
- s[i][j] are in range [1, 9]

Sample Input 0

4 9 2
3 5 7
8 1 5
Sample Output 0

1

Explanation 0

If we change the bottom right value, s[2][2], from 5 to 6 at a cost of |6-5|=1, s becomes a magic square at the minimum possible cost.

Sample Input 1

4 8 2
4 5 7
6 1 6
Sample Output 1

4

"""


def make_sum(first, middle, last, expected_sum):
    if (first + middle + last) == expected_sum:
        return 0
    else:
        return 1


def convert_to_one_d_array(two_d_array, middle_constant):
    one_d_list = []
    for i in two_d_array:
        for j in i:
            one_d_list.append(j)
            # if j not in one_d_list and (j != middle_constant):
            #     one_d_list.append(j)
            # else:
            #     one_d_list.append(0)
    return one_d_list


def formingMagicSquare(s):
    required_moves = 0
    arr_len = len(s)

    one_d_arr_len = arr_len * arr_len

    distinct_sum = 0  # from 1-9, distinct sum is 45.
    for i in range(1, one_d_arr_len + 1):
        distinct_sum += i

    expected_sum = distinct_sum / arr_len  # 15
    middle_constant = expected_sum / arr_len  # 5

    one_d_list = convert_to_one_d_array(s, middle_constant)
    print(f'one_d_list: {one_d_list}')

    half_len = int(one_d_arr_len / 2)
    for i in range(half_len):
        k = half_len + (half_len - i)
        required_moves += make_sum(one_d_list[i], middle_constant, one_d_list[k], expected_sum)
    return required_moves


if __name__ == '__main__':
    # print(formingMagicSquare([[5, 3, 4], [1, 5, 8], [6, 4, 2]]))
    # print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
    # print(formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]]))
    print(formingMagicSquare([[2, 2, 7], [8, 6, 4], [1, 2, 9]])) # 16
