def create_element(n):  # create binary len n
    return n * [0]


def convert_result(array):  # convert result array to string
    result = ''
    for i in array:
        result = result + str(i)
    return result


n = 5
x = create_element(n)
print(x)


def list_binary(i):
    for v in [0, 1]:
        x[i] = v
        if (i == n - 1):
            print(convert_result(x))
        else:
            list_binary(i + 1)


list_binary(0)
