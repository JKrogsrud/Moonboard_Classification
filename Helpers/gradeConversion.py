def font_to_v(grade):
    if grade == "4":
        return 0
    elif grade == "5":
        return 1
    elif grade == "5+":
        return 2
    elif grade == "6A" or grade == "6A+":
        return 3
    elif grade == "6B" or grade == "6B+":
        return 4
    elif grade == "6C":
        return 5
    elif grade == "6C+" or grade == "7A":
        return 6
    elif grade == "7A+":
        return 7
    elif grade == "7B" or grade == "7B+":
        return 8
    elif grade == "7C":
        return 9
    elif grade == "7C+":
        return 10
    elif grade == "8A":
        return 11
    elif grade == "8A+":
        return 12
    elif grade == "8B":
        return 13
    elif grade == "8B+":
        return 14
    elif grade == "8C":
        return 15
    elif grade == "8C+":
        return 16
    elif grade == "9A":
        return 17
    return -1