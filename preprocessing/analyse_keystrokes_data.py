import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("/content/keystroke_processed_data.csv")
print(data.head())

plt.figure(figsize=(12,6))
typing_speed = np.array(data['No of Backspaces'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(typing_speed, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Number of backspaces')
plt.ylabel('Output Label')
plt.title('Scatter Plot with Blue for Label 1, Orange for Label 0')
plt.show()

plt.figure(figsize=(12,6))
typing_speed = np.array(data['Typing Speed']).reshape(-1, 1)
output_label = np.array(data['output_label'])
scaler = StandardScaler()
normalized_typing_speed = scaler.fit_transform(typing_speed)
colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(typing_speed, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Typing Speed')
plt.ylabel('Output Label')
plt.title('Scatter Plot with Blue for Label 1, Orange for Label 0')
plt.show()

plt.figure(figsize=(12,6))
avg_hold_time = np.array(data['Avg Hold Time'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(avg_hold_time, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Avg Hold Time')
plt.ylabel('Output Label')
plt.title('Scatter Plot with Blue for Label 1, Orange for Label 0')
plt.xlim(1,10)
plt.show()

plt.figure(figsize=(12,6))
avg_hold_time = np.array(data['Avg Hold Time'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(avg_hold_time, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Avg Hold Time')
plt.ylabel('Output Label')
plt.title('Scatter Plot with Blue for Label 1, Orange for Label 0')
plt.xlim(2,4)
plt.show()

typing_speed = np.array(data['Typing Speed'])
output_label = np.array(data['output_label'])

mask = (typing_speed <= 1000)
filtered_typing_speed = typing_speed[mask]
filtered_output_label = output_label[mask]

colors = ['blue' if label == 1 else 'orange' for label in filtered_output_label]

plt.scatter(filtered_typing_speed, filtered_output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Typing Speed')
plt.ylabel('Output Label')
plt.title('Filtered and Normalized Scatter Plot (1 to 1000 Range)')
plt.xlim(-100, 100)
plt.show()

max_hold_time = np.array(data['Max Hold Time'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(max_hold_time, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Max Hold Time')
plt.ylabel('Output Label')
plt.xlim(5, 20)
plt.show()

min_hold_time = np.array(data['Min Hold Time'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(max_hold_time, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Min Hold Time')
plt.ylabel('Output Label')
plt.xlim(-5, 20)
plt.show()

avg_keystroke_latency = np.array(data['Avg Keystroke Latency'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(avg_keystroke_latency, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Avg Keystroke Latency')
plt.ylabel('Output Label')
plt.xlim(50, 150)
plt.show()

max_keystroke_latency = np.array(data['Max Keystroke Latency'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(max_keystroke_latency, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Max Keystroke Latency')
plt.ylabel('Output Label')
plt.xlim(-1000, 10000)
plt.show()

min_keystroke_latency = np.array(data['Min Keystroke Latency'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(min_keystroke_latency, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Min Keystroke Latency')
plt.ylabel('Output Label')
plt.xlim(-1000, 10)
plt.show()

avg_digraph_duration = np.array(data['Avg Digraph Duration'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(avg_digraph_duration, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Avg Digraph Duration')
plt.ylabel('Output Label')
plt.xlim(-100, 100)
plt.show()

max_digraph_duration = np.array(data['Max Digraph Duration'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(max_digraph_duration, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Max Digraph Duration')
plt.ylabel('Output Label')
plt.xlim(-100, 500)
plt.show()

min_digraph_duration = np.array(data['Min Digraph Duration'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(min_digraph_duration, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Min Digraph Duration')
plt.ylabel('Output Label')
plt.xlim(-200, 200)
plt.show()

avg_inter_release_latency = np.array(data['Avg Inter-Release Latency'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(avg_inter_release_latency, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Avg Inter-Release Latency')
plt.ylabel('Output Label')
plt.xlim(50, 200)
plt.show()

max_inter_release_latency = np.array(data['Max Inter-Release Latency'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(max_inter_release_latency, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Max Inter-Release Latency')
plt.ylabel('Output Label')
plt.xlim(-100, 800)
plt.show()

min_inter_release_latency = np.array(data['Min Inter-Release Latency'])
output_label = np.array(data['output_label'])

colors = ['blue' if label == 1 else 'orange' for label in output_label]

plt.scatter(min_inter_release_latency, output_label, edgecolors='black', facecolors=colors)
plt.xlabel('Min Inter-Release Latency')
plt.ylabel('Output Label')
plt.xlim(-1000, 800)
plt.show()