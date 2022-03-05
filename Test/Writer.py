
def Utf8toGBK():
    x = (1,2,3)
    res =tuple()
    for value in x:
        value += 1
        res += (value,)
    print(res)


if __name__ == '__main__':
    Utf8toGBK()