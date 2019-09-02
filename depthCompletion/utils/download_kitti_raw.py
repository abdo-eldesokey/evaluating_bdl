# code-checked
# server-checked

import os

# NOTE! NOTE! NOTE! make sure you run this code inside the kitti_raw directory (/root/data/kitti_raw)
kitti_depth_path = "/root/data/kitti_depth"
rgb_depth_path = "/root/data/kitti_rgb"

train_dirs = os.listdir(kitti_depth_path + "/train") # (contains "2011_09_26_drive_0001_sync" and so on)
val_dirs = os.listdir(kitti_depth_path + "/val")

# Create "train" and "val" dir for RGB
rgb_train_dir = os.path.join(rgb_depth_path, "train")
rgb_val_dir = os.path.join(rgb_depth_path, "val")
os.system("mkdir %s" % rgb_train_dir)
os.system("mkdir %s" % rgb_val_dir)

print ("num train dirs: %d" % len(train_dirs))
print ("num val dirs: %d" % len(val_dirs))

# Training set
for step, dir_name in enumerate(train_dirs):
    print("########################### Training set #########################################")
    print("step %d/%d" % (step+1, len(train_dirs)))
    print(dir_name)
    dir_name_no_sync = dir_name.split("_sync")[0] # (dir_name_no_sync == "2011_09_26_drive_0001")

    # download the zip file:
    os.system("wget https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data/%s/%s.zip" % (dir_name_no_sync, dir_name))

    # unzip:
    os.system("unzip %s.zip" % dir_name)

    # move to rgb dir
    zip_dir = dir_name.split('_drive')[0]
    os.system("mv %s %s" % (os.path.join(zip_dir, dir_name), rgb_train_dir))


# Validation set
for step, dir_name in enumerate(val_dirs):
    print("########################### Training set #########################################")
    print("step %d/%d" % (step+1, len(val_dirs)))
    print(dir_name)
    dir_name_no_sync = dir_name.split("_sync")[0] # (dir_name_no_sync == "2011_09_26_drive_0001")

    # download the zip file:
    os.system("wget https://s3.eu-central-1.amazonaws.com/avg-kitti/raw_data/%s/%s.zip" % (dir_name_no_sync, dir_name))

    # unzip:
    os.system("unzip %s.zip" % dir_name)

    # move to rgb dir
    zip_dir = dir_name.split('_drive')[0]
    os.system("mv %s %s" % (os.path.join(zip_dir, dir_name), rgb_val_dir))
