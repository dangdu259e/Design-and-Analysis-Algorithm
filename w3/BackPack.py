class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def getUnitPrice(self):
        return self.value / self.weight

    def toString(self):
        result = "weight: " + str(self.weight) + " value: " + str(self.value)
        return result


def sortItem(listItem):
    for i in range(0, len(listItem)):
        for j in range(i, len(listItem)):
            if (listItem[i].getUnitPrice() < listItem[j].getUnitPrice()):
                temp = listItem[i]
                listItem[i] = listItem[j]
                listItem[j] = temp
    return listItem


# cách dùng vòng lặp for
def laydovaobalo(listItem, maxWeightPack):
    dovatlayra = []
    for i in listItem:
        if (i.getWeight() <= maxWeightPack):
            temp = maxWeightPack // i.getWeight()
            result = i.getWeight() * temp
            maxWeightPack = maxWeightPack - result
            tup = (i, temp)
            dovatlayra.append(tup)
        else:
            continue
    return dovatlayra


item1 = Item(20, 40)
item2 = Item(10, 50)
item3 = Item(15, 80)
listItem = [item1, item2, item3]
print("Dữ liệu đầu vào: ")
for i in listItem:
    print(i.toString())
print("--------------------")
print("Dữ liệu sau khi sắp xếp: ")
listItem = sortItem(listItem)
for i in listItem:
    print(i.toString())
print("--------------------")
dovatlayra = laydovaobalo(listItem, 55)

for i in dovatlayra:
    dovat, soluong = i
    print("do vat lay ra la: " + dovat.toString() + "||" + " Số lượng: " + str(soluong))


# cách dùng đệ quy
def recursion(i, maxWeightPack, weightPack, valuePack):
    if (i > (len(listItem) - 1)):  # trường hợp suy biến
        return weightPack, valuePack
    else:  # trường hợp chạy được
        temp = maxWeightPack // listItem[i].getWeight()  # lấy hệ số
        rou = listItem[i].getWeight() * temp  # cân nặng đồ * hệ số
        newvaluePack = valuePack + (listItem[i].getValue() * temp) #giá trị trong balo sau khi thêm đồ vào
        return recursion(i + 1, maxWeightPack - rou, weightPack + rou, newvaluePack)


weightPack, valuePack = recursion(0, 55, 0, 0)
print("weightPack : {} || valuePack : {}".format(weightPack, valuePack))
