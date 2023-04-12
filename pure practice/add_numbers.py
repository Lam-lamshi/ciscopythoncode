def add_numbers(*args):
    total=0
    for a in args:
        total += a
        print(total)
add_numbers(3)
add_numbers(23)
add_numbers(12)
add_numbers(1,3,4,6,8)