# 1. Import all the code from the file 'module.py'
import module
module.f()

# 2. Rename module in your own file
import module as m
m.f()

# 3. Import only specific functions of the module
from module import f
f()
