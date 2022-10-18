import sys

cmd = sys.argv[1]

exec(cmd)

# python bad.py 'print("Hello, world!")'
# bandit bad.py