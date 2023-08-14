#!/usr/bin/python3
import fileinput
import os
from fnmatch import fnmatch
import re


# 获取当前目录下的指定格式文件
def getFiles(path, suffix):  # suffix为str，示例:   '.txt'      '.json'       '.h5'
    f_list = os.listdir(path)
    res = []
    for file in f_list:
        if fnmatch(os.path.split(file)[1], '*.' + suffix):
            res.append(os.path.join(path, file))
    return res


filename = getFiles(os.getcwd(), "bib")
# filename = "UciMAS.bib"
numFile = filename.__len__()
for i in range(numFile):
    with (fileinput.input(filename[i], encoding='UTF-8', inplace=True) as f):
        for line in f:
            tempLine = line
            if "title" in tempLine and "{{" not in tempLine:
                tempLine = tempLine.replace("{", "{{")
                tempLine = tempLine.replace("}", "}}")
            if "&" in tempLine and "\\&" not in tempLine:
                tempLine = tempLine.replace("&", "\\" + "&")
            if "url" in tempLine:
                tempLine = ""
            if re.search(r"<sub>(.*)</sub>", tempLine):
                result = re.search(r"<sub>(.*)</sub>", tempLine)
                tempLine = tempLine.replace(result.group(0), result.group(1))
            if re.search(r"<i>(.*)</i>", tempLine):
                result = re.search(r"<i>(.*)</i>", tempLine)
                tempLine = tempLine.replace(result.group(0), result.group(1))
            if tempLine != "":
                print(tempLine, end="")

# if "title" in line and "{{" not in line:
#     tempLine = line.replace("{", "{{")
#     tempLine = tempLine.replace("}", "}}")
#     print(tempLine, end="")
#     continue
# elif "&" in line:
#     if "\\&" in line:
#         print(line, end="")
#         continue
#     else:
#         tempLine = line.replace("&", "\\" + "&")
#         print(tempLine, end="")
#         continue
# elif "url" in line:
#     continue
# elif re.search(r"<sub>(.*)</sub>", line) or re.search(r"<i>(.*)</i", line):
#     tempLine = line
#     if re.search(r"<sub>(.*)</sub>", tempLine):
#         result = re.search(r"<sub>(.*)</sub>", line)
#         tempLine = tempLine.replace(result.group(0), result.group(1))
#     if re.search(r"<i>(.*)</i>", tempLine):
#         result = re.search(r"<i>(.*)</i>", tempLine)
#         tempLine = tempLine.replace(result.group(0), result.group(1))
#     print(tempLine, end="")
# else:
#     print(line, end="")
#     continue

# if "title" not in line:
#     if "&" in line:
#         if "\\&" in line:
#             print(line, end="")
#         else:
#             tempLine = line.replace("&", "\\" + "&")
#             print(tempLine, end="")
#     elif "url" in line:
#         continue
#     elif "{{" in line:
#         print(line, end="")
#     else:
#         print(line, end="")
# else:
#     tempLine = line.replace("{", "{{")
#     tempLine = tempLine.replace("}", "}}")
#     print(tempLine, end="")
f.close()
