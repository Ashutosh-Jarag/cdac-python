def div(n1,n2):
    try:
        return n1/n2
    except:
        print("Zero divisible Error")
    finally:
        print("Division completed")

print(div(10,2))
print(div(10,0))


def div1(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Zero divisible Error")
    except TypeError:
        print("Type Error")
    finally:
        print("Division completed")

print(div1(10,2))
print(div1(10,0))
print(div1(10,"a"))