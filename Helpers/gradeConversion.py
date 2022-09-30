def font_to_v(grade):
    if grade == "4":
        return 0
    elif grade == "5":
        return 1
    elif grade == "5+":
        return 2
    elif grade == "6a" or grade == "6a+":
        return 3
    elif grade == "6b" or grade == "6b+":
        return 4
    elif grade == "6c":
        return 5
    elif grade == "6c+" or grade == "7a":
        return 6
    elif grade == "7a+":
        return 7
    elif grade == "7b" or grade == "7b+":
        return 8
    elif grade == "7c":
        return 9
    elif grade == "7c+":
        return 10
    elif grade == "8a":
        return 11
    elif grade == "8a+":
        return 12
    elif grade == "8b":
        return 13
    elif grade == "8b+":
        return 14
    elif grade == "8c":
        return 15
    elif grade == "8c+":
        return 16
    elif grade == "9a":
        return 17
    return -1