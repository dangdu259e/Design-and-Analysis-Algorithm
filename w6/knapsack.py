class Item:  # define item
    def __init__(self, weight, value):
        self.value = value
        self.weight = weight

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    # get unit price in item = value / weight
    def getUnitPrice(self):
        return self.value / self.weight

    def toString(self):
        result = "weight: " + str(self.weight) + " value: " + str(self.value)
        return result


# print list item in string
def print_listItem(listItem):
    for i in listItem:
        print("(" + str(i.toString()) + ")", end=',')
    print()


def sortItem(listItem):
    for i in range(0, len(listItem)):
        for j in range(i, len(listItem)):
            if (listItem[i].getUnitPrice() < listItem[j].getUnitPrice()):
                temp = listItem[i]
                listItem[i] = listItem[j]
                listItem[j] = temp
    return listItem


# 0 - 1 knapsack using greedy
def knapSack(listItem, max_weight_backpack):
    print("list item input: ")
    print_listItem(listItem)
    listItem = sortItem(listItem)
    print("list item after short: ")
    print_listItem(listItem)
    total_value = 0
    solution = [0 for i in range(0, len(listItem))]
    for i in range(0, len(listItem)):
        if (i == len(listItem) - 1):
            if (listItem[i].getWeight() <= max_weight_backpack):
                solution[i] = 1
                max_weight_backpack -= int(listItem[i].getWeight())
                total_value += int(listItem[i].getValue())
                return total_value, solution
            else:
                return total_value, solution
        else:
            solution[i] = 1
            max_weight_backpack -= int(listItem[i].getWeight())
            total_value += int(listItem[i].getValue())


# Mẫu thử tạo bằng tay
item1 = Item(10, 60)
item2 = Item(20, 100)
item3 = Item(30, 120)
listItem = [item1, item2, item3]
max_weight_backpack = 50
total_value, solution = knapSack(listItem, max_weight_backpack)
print("total_value = " + str(total_value))
print("solution = " + str(solution))
