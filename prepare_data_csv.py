###
from glob2 import glob
import pandas as pd
import argparse
import os
from tqdm import tqdm
import json

def get_list_image_to_csv(lst_train, output_path, id2id_encode, drop_minor_class= False):
  csv_content = []
  for img_path in lst_train:
    split_img = img_path.split("/")
    image_name = split_img[-1]
    class_id = split_img[-2]
    csv_content.append({
        'filepath': img_path,
        'image_name':image_name,
        'id': class_id,
        'id_encode': id2id_encode[class_id]
    })

  df = pd.DataFrame(csv_content)
  if drop_minor_class == True:
    del_list = ['cornmarket', 'hertford','oriel','pitt_rivers','worcester']
    df = df.drop(df[df.id.isin(del_list)].index)
    df.to_csv(output_path, index=False)
  else:
    df.to_csv(output_path, index=False)
  print("DONE")
def parse_args():

  parser = argparse.ArgumentParser()
  parser.add_argument('--data_path', type=str, required=True)
  parser.add_argument('--output_path', type=str, required=True)
  parser.add_argument('--drop_minor_class', action='store_true')
  args, _ = parser.parse_known_args()
  return args

if __name__ == "__main__":
  args = parse_args()
  lst_class = glob(f"{args.data_path}/*")
  lst_class.sort()

  id2id_encode = {x.split("/")[-1]:idx for idx, x in enumerate(lst_class)}
  json.dump(id2id_encode, open(f"{args.data_path}/id2id_encode.json", "w"))

  lst_train, lst_val = [], []
  for class_name in tqdm(lst_class):
    lst_img = os.listdir(class_name)
    lst_train.extend(list(map(lambda x: f'{class_name}/{x}', lst_img[:-10])))
    lst_val.extend(list(map(lambda x: f'{class_name}/{x}', lst_img[-10:])))

  os.makedirs(args.output_path, exist_ok=True)
  if args.drop_minor_class:
    get_list_image_to_csv(lst_train, f'{args.output_path}/train.csv', id2id_encode, drop_minor_class=True)
    get_list_image_to_csv(lst_val, f'{args.output_path}/val.csv', id2id_encode, drop_minor_class=True)
  else:
    get_list_image_to_csv(lst_train, f'{args.output_path}/train.csv', id2id_encode)
    get_list_image_to_csv(lst_val, f'{args.output_path}/val.csv', id2id_encode)