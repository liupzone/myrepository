import os
path_sr="/home/lpzone/dataset/NasData/车道/86_case/road_perception_benchmark/dataset_m3/系数评价/benchmark_res/version_1.0.7.1"
path_dst="/media/lpzone/cve_drive3/奇瑞-车道线评测/对比结果"

for root, dirs, files in os.walk(path_sr):
    for file in files:
        if file == "left_line.eps" or file == "right_line.eps":
            # print(root)
            eval_pic = os.path.join(root, file)
            # print(eval_pic)
            eval_res = os.path.basename(root)
            case_name = os.path.basename(os.path.dirname(root))
            scene_name = os.path.basename(os.path.dirname(os.path.dirname(root)))
            dst_dir = os.path.join(path_dst, scene_name)
            dst_dir = os.path.join(dst_dir, case_name)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            cmd_str1 = "cp -v {} {}".format(eval_pic, dst_dir)
            
            os.system(cmd_str1)

