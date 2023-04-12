def get_gender(sex="unknowwn"):
    if sex in "m":
        sex="male"
    elif sex in "f":
        sex="female"
    print(sex)
get_gender("m")
get_gender("f")
get_gender()