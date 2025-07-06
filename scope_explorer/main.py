x = 10  # Global

def outer():
    x = 20  # Local to outer
    def inner():
        nonlocal x
        x = 30
        print("Inner x:", x)
    inner()
    print("Outer x after inner:", x)

outer()
print("Global x:", x)
