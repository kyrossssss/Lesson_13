from functions import salary, hello_who

def test_hello_who_max():
    assert hello_who("Max") == 'hello, Max'

# def test_ajlfdw():
#     assert hello_who("Jack") == "hello, Jack"
#     assert hello_who("Tom") == "hello, Tom"
#     assert hello_who("Sam") == "hello, Sam"
#     assert hello_who("Ted") == "hello, Ted"


def test_salary():
    assert salary(2, 2) != 8
    assert salary(3, 1) != 6