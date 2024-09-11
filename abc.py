class abc:
    def __init__(instanz, value):
        instanz.value = value

    def show_value(instanz):
        print(f"The Value is {instanz.value}")

x = abc(5)
x.show_value()

