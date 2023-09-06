def greet(fx):
    def mfx():
        print('good morning')
        fx()
        print('thanks for using this function')
    return mfx


@greet
def hello():
    print('hello')


def add(a, b):
    print(a + b)


hello()
