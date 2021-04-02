import random

# coin_real > coin_fake
coin_real = 2
coin_fake = 1


# tạo ngẫu nhiên listcoint có size = n
def random_coins(n):
    """A shuffled list of (n-1) real coins and 1 fake coin."""
    assert n > 0
    coins = [coin_real] * (n - 1) + [coin_fake] * (1)
    random.shuffle(coins)
    return coins


# tính tổng cân nặng coin trong list từ s đến e
def sumCoin(listcoin, s, e):  # sum[s,e]
    sum = 0
    for i in range(s, e + 1):
        sum += listcoin[i]
    return sum


# tìm đồng xu giả
def find_fake_coin(list_coin, s, e):
    n = (e - s) + 1
    if (n % 2 == 0):
        mid = n // 2 - 1 + s
        sum_left = sumCoin(list_coin, s, mid)
        sum_right = sumCoin(list_coin, mid + 1, e)
        if (sum_left == sum_right):
            return None
        elif (sum_left < sum_right):
            return find_fake_coin(list_coin, s, mid)
        else:
            return find_fake_coin(list_coin, mid + 1, e)
    else:
        mid = n // 2 + s
        sum_left = sumCoin(list_coin, s, mid - 1)
        sum_right = sumCoin(list_coin, mid + 1, e)
        if (sum_left == sum_right):
            return mid
        elif (sum_left < sum_right):
            return find_fake_coin(list_coin, s, mid - 1)
        else:
            return find_fake_coin(list_coin, mid + 1, e)

#kiểm tra 1 lần với danh sách đồng xu cố định
print("* kiểm tra 1 lần với chuỗi cố định ")
list_coin = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(list_coin)
print("Fake Coin Position: "+str(find_fake_coin(list_coin=list_coin, s=0, e=(len(list_coin) - 1))))
print("-----------------------")

#kiểm tra 1 lần với danh sách đồng xu ngẫu nhiên
print("* kiểm tra 1 lần với danh sách đồng xu ngẫu nhiên ")
list_coin = random_coins(10)
print(list_coin)
print("Fake Coin Position: "+str(find_fake_coin(list_coin=list_coin, s=0, e=(len(list_coin) - 1))))
print("-----------------------")

#kiểm tra n lần với danh sách đồng xu ngẫu nhiên
print("* kiểm tra n lần với danh sách đồng xu ngẫu nhiên")
print("Nhập vào số lần bạn muốn kiểm tra: ")
n = int(input())
for i in range(0, n):
    list_coin = random_coins(10)
    print(list_coin)
    print("Fake Coin Position: "+str(find_fake_coin(list_coin=list_coin, s=0, e=(len(list_coin) - 1))))
    print("-----------------------")
