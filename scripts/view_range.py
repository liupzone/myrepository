
import json
from matplotlib import pyplot as plt
pcv_log = "/home/lpzone/work_folder/socket_hil/protobuf_cv22_20210602/protobuf_cv22/cv22_data/20210819211629/20210819211629.txt"
view_end_list = []
right_view_end = []
delays = []
with open(pcv_log, 'r') as pcv_fi:
    lines = pcv_fi.readlines()
    for line in lines:
        line_json = json.loads(line)
        # print(line_dict)
        if "type" in line_json and line_json['type'] == "roadmarking":
            road_mark = line_json['roadmarking']
            laneline = road_mark['laneline']
            if bool(laneline):
                lanes = laneline['line']
                delays.append(road_mark['finish_time'])
                for lane in lanes:
                    if "pos_type" in lane:
                        pos_type = lane['pos_type']
                        if pos_type == "kEgoLeft":
                            curve_vehicle_coord = lane['curve_vehicle_coord']
                            view_end = curve_vehicle_coord["longitude_max"]
                            view_end_list.append(view_end)
                            print(view_end)

frame_id = []
for i in range(len(view_end_list)):
    frame_id.append(i)

plt.title("ego_left_view_end") 
plt.xlabel("frame_id") 
plt.ylabel("view_end") 
plt.plot(frame_id,view_end_list) 
plt.show()