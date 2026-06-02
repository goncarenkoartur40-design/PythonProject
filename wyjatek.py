try:
    a = 10
    b = "0"
    wynik = a/b
    print(wynik)
except TypeError:
    print("niepoprawna liczba")
except ZeroDivisionError:
    print("nie mozna dzielic przez 0")
finally:
    print("tu bedzie jakas czeszc programu")

