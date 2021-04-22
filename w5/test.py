def create_element(n):  # create binary len n
    return n * [0]


def convert_result(array):  # convert result array to string
    result = ''
    for i in array:
        result = result + str(i)
    return result


def Permutation(array):
    n = len(array)
    if (n == 0):
        return []
    elif (n == 1):
        return [array]
    else:
        # create empty list
        per = []
        for i in range(0, len(array)):
            x = array[i]
            # print("***********")
            # print(array[:i])
            # print(array[i + 1:])
            # print("***********")

            remaining_list = array[:i] + array[i + 1:]

            for p in Permutation(remaining_list):
                per.append([x] + p)

        return per


# data = list('1234')
data = [1, 2, 3, 4]
print("data: "+ str(data))
print("Các hoán vị của data")
for p in Permutation(data):
    print(convert_result(p))
