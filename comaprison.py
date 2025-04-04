import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

# Load the XML file
xml_file = "classifier.xml"
tree = ET.parse(xml_file)
root = tree.getroot()

# Extract labels
labels = []
for label in root.find("recognizer/labels"):
    labels.append(int(label.text))

# Extract histograms
histograms = []
for hist in root.find("recognizer/histograms"):
    hist_data = eval(hist.text)  # Convert string to list
    histograms.append(hist_data)

# Convert to NumPy array for easier processing
histograms = np.array(histograms)

# Calculate the sum of histogram values per label (for bar chart)
hist_sums = histograms.sum(axis=1)

# Plot Bar Chart (Sum of Histograms for Each Label)
plt.figure(figsize=(10, 5))
plt.bar(labels, hist_sums, color='blue', alpha=0.6, label="Histogram Sum")
plt.xlabel("Labels (Face ID)")
plt.ylabel("Histogram Sum")
plt.title("LBPH Training Histogram Sum per Face ID")
plt.legend()
plt.show()

# Plot Line Graph (Histogram Data for Each Label)
plt.figure(figsize=(10, 5))
for i, hist in enumerate(histograms):
    plt.plot(range(len(hist)), hist, marker='o', label=f"Face ID {labels[i]}")

plt.xlabel("Histogram Index")
plt.ylabel("Histogram Value")
plt.title("LBPH Histogram Features for Faces")
plt.legend()
plt.show()

