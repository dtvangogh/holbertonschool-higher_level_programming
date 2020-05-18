#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_array = []
    for i in range (0, len(my_list_2)):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0

        finally:
            new_array.append(result)
    return new_array