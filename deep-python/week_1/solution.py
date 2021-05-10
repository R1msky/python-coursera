import sys

digit_string = sys.argv[1]
digit_string = [int(i) for i in digit_string]


print(sum(list(digit_string)))
