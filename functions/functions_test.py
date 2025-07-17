"""question number 1"""
"""Write a Python function to find the maximum of three numbers."""
def find_max_of_three(x, y, z): 
    re = max([x,y,z])
    return re
# print(find_max_of_three(434,2,-22))

"""question number 2"""
"""Write a Python function to sum all the numbers in a list."""
def get_list_sum(list):
    re = 0
    for num in list: 
        re += num
    return re
# print(get_list_sum([434,2,-22]))

"""question number 3"""
"""Write a Python program to reverse a string."""
def string_reverse(input_str):
    temp_list = list(input_str)
    temp_list.reverse()
    reversed_string = "".join(temp_list)
    return reversed_string
# print(string_reverse("hello, word!"))

"""question number 4"""
"""Write a Python function to calculate the factorial of a number (a non-
negative integer). The function accepts the number as an argument."""
def calculate_factorial(number):
    if number == 0:
        return 1
    return calculate_factorial(number - 1) * number
# print(calculate_factorial(5))

"""question number 5"""
"""Write a Python function to check whether a number falls within a given range."""
def check_if_number_in_range(number, range):
    if number in range:
        return True
    return False
# print(check_if_number_in_range(44, range(3, 99)))

"""question number 6"""
"""Write a Python function that accepts a string and counts the number of upper and lower case letters."""
def get_user_input_and_find_number_of_odd_and_even():
    while True:
        try:
            user_input = input("give me the number of list count:")
            user_input_int = int(user_input)
        except ValueError as error:
            print("the input most be only number")
            continue
        break
    i = 0
    list = [] 
    while i < user_input_int:
        while True:
            try :
                input_number = input("give me the number that has to be added to the list:")
                input_number_int = int(input_number)
            except ValueError as error:
                print("the input most be only number")
                continue
            break
        list.append(input_number_int)
        i += 1
    odd = 0
    even = 0
    print(list)
    for x in list:
        if x % 2 == 0:
            even += 1
        else: 
            odd += 1
    return ('even=', even, 'odd=', odd)
# print(get_user_input_and_find_number_of_odd_and_even())

"""question number 7"""
"""Write a Python function that takes a list and returns a new list with distinct elements from the first list."""
def get_distinct_elements_from_list(input_list):
    re = []
    for x in input_list:
        if input_list.count(x) == 1:
            re.append(x)
    return re
# print(get_distinct_elements_from_list([1,2,3,4,4,4,54,5,5]))

"""question number 8"""
"""Write a Python function that takes a number as a parameter and checks whether the number is prime or not."""
# AI
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
# print(is_prime(5))

"""question number 9"""
"""Write a Python function to check whether a number is "Perfect" or not."""
# AI
def is_perfect(number):
    if number < 2:
        return False
    list = []
    for i in range(1, number):
        if number % i == 0:
            list.append(i)
    return sum(list) == number
# print(is_perfect(6))

"""question number 10"""
"""Write a function count_vowels(s) that counts the number of vowels (a, e, i, o, u) in a given string."""
def count_vowels(s):
    count = 0
    for c in s:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            count += 1
    return count
# print(count_vowels("hello world"))

"""question number 11"""
"""Sort a List Without Using sort()
Write a function custom_sort(lst) that sorts a list without using"""
# AI
def custom_sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
# print(custom_sort([3, 1, 4, 2]))

"""question number 12"""
""""Count Words in a Sentence
Write a function count_words(sentence) that returns the number of words in a given sentence."""
def count_words(sentence):
    words = sentence.split()
    return len(words)
# print(count_words("Hello, how are you?"))

"""question number 13"""
"""Write a Python program to count the number of characters (character frequency) in a string."""
def get_character_frequency(str):
    dict = {}
    for x in str:
        dict[x] = str.count(x)
    return dict
# print(get_character_frequency("Hello, World!"))

"""question number 14"""
"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string."""
def join_swap_first_two_characters(str1, str2):
    re1 = str2[:2] + str1[2:]
    re2 = str1[:2] + str2[2:]
    return re1 + " " + re2
# print(join_swap_first_two_characters("abc", "xyz"))

"""question number 15"""
"""Write a Python function that takes a list of words and return the longest word and the length of the longest one."""
def find_longest_word(list):
    longest_word = ""
    for word in list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word, len(longest_word)
# print(find_longest_word(["hello", "world!"]))

"""question number 16"""
"""Write a Python program to remove characters that have odd index values in a given string."""
# AI
def remove_odd_index_characters(str):
    return str[::2]
# print(remove_odd_index_characters("Hello, World!"))

"""question number 17"""
"""Write a Python script that takes input from the user and displays that input back in upper and lower cases."""
def display_user_input():
    user_input = input("Enter a string: ")
    print("upper:", user_input.upper())
    print("lower:", user_input.lower())
# display_user_input()

"""question number 18"""
"""Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)."""
def get_copies_of_last_two_characters(str):
    if len(str) < 2:
        return "String must be at least 2."
    last_two = str[-2:]
    return last_two * 4
# print(get_copies_of_last_two_characters("Hello"))

"""question number 19"""
"""Write a Python function to reverse a string if its length is a multiple of 4."""
def reverse_string_if_multiple_of_four(str):
    if len(str) % 4 == 0:
        return str[::-1]
    return str
# print(reverse_string_if_multiple_of_four("12345678"))

"""question number 20"""
"""Write a Python program to check whether a string starts with specified characters."""
def check_string_starts_with(str, chr):
    return str.startswith(chr)
# print(check_string_starts_with("Hello, World!", "Hello"))

"""question number 21"""
"""Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples."""
def temp_func(t):
    return t[-1]
def sort_by_last_element_in_tuple(tuples_list):
    return tuples_list.sort(key=temp_func)
# print(sort_by_last_element_in_tuple([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

"""question number 22"""
"""Write a Python program to remove duplicates from a list."""
def remove_duplicates_from_list(input_list):
    return list(set(input_list))
# print(remove_duplicates_from_list([1, 2, 3, 4, 4, 5, 5, 6]))

"""question number 23"""
"""Write a Python program to check if a list is empty or not."""
def is_list_empty(input_list):
    return len(input_list) == 0
# print(is_list_empty([]))

"""question number 24"""
"""Write a Python program to insert an element before each element of a list."""
def insert_element_before_each(input_list, element):
	new_list = []
	for item in input_list:
		new_list.append(element)
		new_list.append(item)
	return new_list
# print(insert_element_before_each([1, 2, 3], 'x'))

"""question number 25"""
"""Write a Python program to compute the difference between two lists."""
def compute_difference_between_two_list(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.symmetric_difference(set2))
# print(compute_difference_between_two_list(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]))

"""question number 26"""
"""Write a Python program to convert a string to a list."""
def convert_string_to_list(input_str):
    return input_str.split()
# print(convert_string_to_list("Hello World"))

"""question number 27"""
"""Write a Python program to convert a list to a tuple."""
def convert_list_to_tuple(input_list):
    return tuple(input_list)
# print(convert_list_to_tuple([1, 2, 3]))