from glob2 import glob
import os
from tqdm import tqdm
import argparse

def parse_args():

  parser = argparse.ArgumentParser()
  parser.add_argument('--data_path', type=str, required=True)
  args, _ = parser.parse_known_args()
  return args

if __name__ == "__main__":
    args = parse_args()
    lst_img = glob(f"{args.data_path}/*.jpg")
    for img_path in tqdm(lst_img):
      split_img_path = img_path.split("/")
      class_folder = "_".join(split_img_path[-1].split("_")[:-1])
      folder_path = f'{"/".join(split_img_path[:-1])}/{class_folder}'
      os.makedirs(folder_path, exist_ok = True)
      os.system(f"mv {img_path} {folder_path}/{split_img_path[-1]}")