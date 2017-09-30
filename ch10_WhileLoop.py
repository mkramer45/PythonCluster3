my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

start_number = 0  # this 0 references the array of my list in our while statement

while start_number < 5:  # starts at 0 via our variable declaration
    print(my_list[start_number])  # will start at 1
    start_number += 1  # this will increment our start number so it won't always remain at 0 ... if not for this, remaining at 0 would result in infinite loo

