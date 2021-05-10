import sys

arg = sys.argv[1]
n = int(arg)

for i in range(1, n+1):
	tree = " "* (n-i) +"#"*i
	print(tree)



