import pandas as pd
import matplotlib.pyplot as plt
import argparse
import matplotlib.pylab as pylab
from glob2 import glob

params = {'legend.fontsize': 'large',
          'figure.figsize': (20, 8),
         'axes.labelsize': 'large',
         'axes.titlesize':'large',
         'xtick.labelsize':'large',
         'ytick.labelsize':'large'}

pylab.rcParams.update(params)

plt.style.use("seaborn")

def parse_args():

  parser = argparse.ArgumentParser()
  parser.add_argument('--save_loss_path', type=str, required=True)
  parser.add_argument('--output_path', type=str, required=True)
  args, _ = parser.parse_known_args()
  return args

def visualize(data_csv, output_path):
    data_csv.plot()
    plt.savefig(output_path)

if __name__ == "__main__":
    save_loss_path = 'save_loss'
    lst_csv = glob(f'{save_loss_path}/**/*.csv')
    for csv_path in lst_csv:
        output_path = f'{csv_path[:-4]}_summary'
        print(output_path)
        df = pd.read_csv(csv_path)
        visualize(df, output_path)