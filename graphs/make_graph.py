import numpy as np
import os
import matplotlib.pyplot as plt
import argparse

def plot(file):
  f = open(file, 'r')
  lines = f.readlines()
  x, y = [], []
  for line in lines[1:]:
    vals = line.rstrip('\n').split(',')
    vals = list(map(float, vals))
    x.append(vals[1])
    y.append(vals[2])
  
  plt.plot(x, y)
  plt.grid(True)
  plt.ylim(0, 1)
  plt.xlim(min(x), max(x))
  if "mAP" in file:
    plt.ylabel("mAP")
    plt.xlabel("Number of epochs")
    plt.title("Validation mAP")
  elif "precision" in file:
    plt.ylabel("Precision")
    plt.xlabel("Number of epochs")
    plt.title("Validation precision")
  elif "recall" in file:
    plt.ylabel("Recall")
    plt.xlabel("Number of epochs")
    plt.title("Validation recall")
  plt.savefig(file.split('.')[0]+".png", transparent=True)
    

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Parse .csv")
  parser.add_argument("-f", "--file", type=str, default="mAP-depth-filter120e.csv", help="Path to .csv file")
  args = parser.parse_args()
  plot(args.file)
