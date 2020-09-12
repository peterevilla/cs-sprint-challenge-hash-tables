def has_negatives(a):
   
    dictionary = {}  # a hashtable to store values
    result = []
    for num in a:
        if abs(num) in dictionary:
            result.append(abs(num))
        else:
            dictionary[abs(num)] = abs(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
