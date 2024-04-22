import random
import matplotlib.pyplot as plt
import numpy as np
from Sample import times

def main(length):
  # Get the times for sorting algorithms
  samples = []
  t1=[]
  t2=[]
  t3=[]
  # Plot the times for each algorithm separately
  for i in range(100):
      sorting_times = times(1, length)
      samples.append(i)
      t1.append(sorting_times[0])
      t2.append(sorting_times[1])
      t3.append(sorting_times[2])
        # Time corresponding to each sample
  avg1 = np.mean(t1)
  avg2 = np.mean(t2)
  avg3 = np.mean(t3)

  # Create figure and subplots
  fig, axes = plt.subplots(1, 3, figsize=(15, 5))
  # Plotting the first scatter plot
  axes[0].scatter(samples, t1)
  axes[0].axhline(avg1, color='red', linestyle='--', label=f'Average: {avg1:.2f}')
  axes[0].text(105, avg1, f'{avg1:.2f}', ha='left', va='center')
  axes[0].set_title(f'Quick Sort\n List Length = {length}')
  axes[0].set_xlabel('Samples')
  axes[0].set_ylabel('Time (ms)')
  axes[0].set_ylim([0, t3[0]/10])

  # Plotting the second scatter plot
  axes[1].scatter(samples,t2)
  axes[1].axhline(avg2, color='red', linestyle='--', label=f'Average: {avg2:.2f}')
  axes[1].text(105, avg2, f'{avg2:.2f}', ha='left', va='center')
  axes[1].set_title(f'Merge Sort\n List Length = {length}')
  axes[1].set_xlabel('Samples')
  axes[1].set_ylabel('Time (ms)')
  axes[1].set_ylim([0, t3[0]/10])

  # Plotting the third scatter plot
  axes[2].scatter(samples, t3)
  axes[2].axhline(avg3, color='red', linestyle='--', label=f'Average: {avg3:.2f}')
  axes[2].text(105, avg3, f'{avg3:.2f}', ha='left', va='center')
  axes[2].set_title(f'Insertion Sort\n List Length = {length}')
  axes[2].set_xlabel('Samples')
  axes[2].set_ylabel('Time (ms)')
  axes[2].set_ylim([0, t3[0]*1.5])

  # Adjust layout
  plt.tight_layout()

  # Show plots
  plt.show()
main(10000)