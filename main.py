

def myfunc(x, y):
    z = 2 * x - y + 100
    return z


def myfunc_3(a):
    for i in range(5):
        myfunc(a[i], a[i + 1])


def myfunc_4(a):
    z = a[1] + a[2] + a[3] - a[4]



def main():
    a = [1, 2, 3, 4, 5]
    for _ in range(100):
        myfunc_4(a)
    for _ in range(300):
        myfunc_3(a)


if __name__ == '__main__':
    main()
