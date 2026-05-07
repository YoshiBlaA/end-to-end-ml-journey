#Write a Python program that uses the filter function to extract all uppercase letters from a list of mixed-case strings.

mixed_case_strings = ["Hello", "w3resource", "Python", "Filter", "Learning"]

upper_case_letters = filter(lambda x: x.isupper(), "".join(mixed_case_strings))

print(list(upper_case_letters))