coin = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]
# coin_real > coin_fake
import random
import enum

Scale = enum.Enum(
    "Scale", ["LeftHeavy", "RightHeavy", "Balanced"]
)

coin_real = 2
coin_fake = 1


def random_coins(n):
    """A shuffled list of (n-1) real coins and 1 fake coin."""
    assert n > 0
    coins = [coin_real] * (n - 1) + [coin_fake] * (1)
    random.shuffle(coins)
    return coins


def sumCoin(listcoin, s, e):  # sum[s,e]
    sum = 0
    for i in range(s, e + 1):
        sum += listcoin[i]
    return sum


# def find_fake_coin(listcoin, s, e, pivot):  # listcoin, 0, 9
# n = e - s + 1
# # Chuỗi lẻ
# if (n % 2 != 0):
#     # điểm ở giữa
#     mid = int((e - s) // 2) + chot
#     sum_left = sumCoin(listcoin, 0, mid-1)
#     sum_right = sumCoin(listcoin, mid+1, n-1)
#     if (sum_left == sum_right):
#         return mid
#     elif (sum_left > sum_right):  # right => (mid+1 , e)
#         chot = chot + mid
#         return find_fake_coin(listcoin, mid + 1, e, chot)
#     else:  # left => (s, mid-1)
#         chot = chot - mid
#         return find_fake_coin(listcoin, s, mid - 1, chot)
# # chuỗi chẵn
# else:
#     # điểm ở giữa
#     # mid = none
#     note = (e - s) // 2  # note = 4
#     sum_left = sumCoin(listcoin, 0, note)  # left = (0, note)
#     sum_right = sumCoin(listcoin, note + 1, e)  # right = (note+1, n)
#     print(sum_left)
#     print(sum_right)
#     if (sum_left == sum_right):
#         return None
#     elif (sum_left > sum_right):
#         return find_fake_coin(listcoin, note + 1, e)  # left > right => right =>  (note+1, e)
#     else:
#         return find_fake_coin(listcoin, s, note)  # left < right => left => (0, note)
def find_fake_coin(list_coin, s, e, pivot):
    n = (e - s) + 1
    if (n % 2 == 0):
        mid = n // 2 - 1
        sum_left = sumCoin(list_coin, s, mid)
        sum_right = sumCoin(list_coin, mid + 1, e)
        if (sum_left == sum_right):
            return None
        elif (sum_left < sum_right):
            if(pivot > mid):
                pivot = pivot - mid
            else:
                pivot = pivot + mid
            return find_fake_coin(list_coin, s, mid, pivot)
        else:
            pivot = pivot + mid
            return find_fake_coin(list_coin, mid + 1, e, pivot)
    else:
        mid = n // 2
        sum_left = sumCoin(list_coin, s, mid)
        sum_right = sumCoin(list_coin, mid + 1, e)
        if (sum_left == sum_right):
            return mid
        elif (sum_left < sum_right):
            pivot = pivot - mid
            return find_fake_coin(list_coin, s, mid, pivot)
        else:
            pivot = pivot + mid
            return find_fake_coin(list_coin, mid + 1, e, pivot)



# list_coin = random_coins(10)
list_coin = [2, 2, 2, 1, 2, 2, 2, 2, 2, 2]
print(len(list_coin))
print(list_coin)
print(find_fake_coin(list_coin=list_coin, s=0, e=(len(list_coin) - 1), pivot=0))
