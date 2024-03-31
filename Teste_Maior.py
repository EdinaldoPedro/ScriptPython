def maior (a,b):
    if a > b:
        return print(a)
    else:
        return print(b)

def test_maior1():
    assert maior(0,1) == 1

def test_maior2():
    assert maior(2,1) == 2

def test_maior3():
    assert maior(0,3) == 3

def test_maior42():
    assert maior(415,144) == 415