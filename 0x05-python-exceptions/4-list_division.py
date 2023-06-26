#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    try:
        for a in range(list_length):
            try:
                elem1 = my_list_1[a]
                elem2 = my_list_2[a]
                div_res = elem1 / elem2
                res.append(div_res)
            except ZeroDivisionError:
                res.append(0)
                print("division by 0")
            except (TypeError, ValueError):
                res.append(0)
                print("wrong type")
            except IndexError:
                print("out of range")
                break
    finally:
        return res
