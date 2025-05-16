import numpy as np
from collections import Counter
from PIL import Image
from sklearn.cluster import KMeans

def extract_colors(img, num_colors):
    # Convert image to a numpy array and reshape it
    img_data = np.array(img)
    img_data = img_data.reshape((-1, 3))  # Flatten to a 2D array of pixels

    # Count occurrences of each color
    counter = Counter(tuple(pixel) for pixel in img_data)
    
    # Get the top 'num_colors' most common colors
    common_colors = counter.most_common(num_colors)
    
    # Convert RGB to HEX
    hex_colors = [(r, g, b) for (r, g, b), _ in common_colors]
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in hex_colors]
    
    return hex_colors

def get_dominant_colors(image_path, k=10):
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB mode
    img_data = np.array(img)
    
    # Reshape the image to a 2D array where each pixel is a data point
    img_data = img_data.reshape((-1, 3))
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(img_data)
    
    # Get the RGB values of the cluster centers
    colors = kmeans.cluster_centers_
    colors = colors.round(0).astype(int)
    
    # Convert RGB to HEX and return
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(int(r), int(g), int(b)) for r, g, b in colors]
    
    return hex_colors