
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def main():
    print("Hello, Jenkins!")
    print("Automatic CI build triggered successfully!")
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(10, 4))
    print("Multiplication:", multiply(5, 3))
    print("GitHub webhook integration successful!")
    print("Automated Docker deployment successful!")


if __name__ == "__main__":
    main()
