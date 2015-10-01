import commands
import sys
import os
# import shutil

directory = sys.argv[1]
cmd = 'ls /' + directory
(status, output) = commands.getstatusoutput(cmd)
print output


# filenames = os.listdir(directory)
# print filenames
# for filename in filenames:
# 	path = os.path.join(directory, filename)
# 	print path
# 	print os.path.abspath(path)