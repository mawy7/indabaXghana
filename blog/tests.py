
# Create your tests here.
def manu(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    else:
        return manu(x - 1) + manu(x-2)


print(manu(10))