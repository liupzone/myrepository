
import json
file_list = "/home/lpzone/dataset/junction/j.list"
merge = 0
split = 0
list_f = open(file_list, "r")
lines = list_f.readlines()

for fi in lines:
    fi = fi.strip()
    print("json: ", fi)
    with open(fi, "r") as jf:
        data_j = json.load(jf)
        if len(data_j) == 0:
            continue
        print(data_j[0])
        if "intersection_point" in data_j[0]["label"] and "junction" in data_j[0]['label']:
            merge += 1
        if "intersection_point" in data_j[0]["label"] and "branch" in data_j[0]['label']:
            split += 1

print("merge: ", merge)
print("split: ", split)