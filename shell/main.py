from sh import ls
from sh import az

# note that sh is OS specific, this on works on linux
print(ls('-lhat'))

print(az('--version'))

