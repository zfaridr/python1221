import os
import sys
import shutil
category_1 = 0
category_2 = 0
category_3 = 0
category_4 = 0

for root, dirs, files in os.walk('my_project'):
    for file in files:
        if len(file) <= 100:
            category_1 = category_1 + 1
        elif len(file) <= 1000:
            category_2 = category_2 + 1
        elif len(file) <= 10000:
            category_3 = category_3 + 1
        else:
            category_4 = category_4 + 1

stat = {
    100: category_1,
    1000: category_2,
    10000: category_3,
    100000: category_4
}

print(stat)
