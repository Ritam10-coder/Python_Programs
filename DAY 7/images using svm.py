import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset and prepare the data
# TensorFlow provides datasets such as the Flowers dataset, but here we will use a custom dataset.

# For demonstration, you can use your own flower dataset with ImageDataGenerator
# Assuming you have a directory with subdirectories for each flower category
data_dir = 'path_to_your_flower_dataset'  # Update this path to your dataset

# Data augmentation and preprocessing
datagen = ImageDataGenerator(preprocessing_function=preprocess_input)

# Load and preprocess the data
batch_size = 32
image_size = (224, 224)
data = datagen.flow_from_directory(data_dir, target_size=image_size, batch_size=batch_size, class_mode='categorical', shuffle=False)
class_labels = list(data.class_indices.keys())

# Load pre-trained VGG16 model + higher level layers
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Extract features using VGG16
features = base_model.predict(data)
features = features.reshape(features.shape[0], -1)  # Flatten the features

# Encode the labels
le = LabelEncoder()
labels = le.fit_transform(data.classes)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Create an SVM classifier
svm_classifier = SVC(kernel='linear', C=1.0)

# Train the classifier
svm_classifier.fit(X_train, y_train)

# Make predictions
y_pred = svm_classifier.predict(X_test)

# Evaluate the classifier
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=class_labels))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# If you want to visualize some results:
import matplotlib.pyplot as plt
import cv2

# Display some test images along with their predicted labels
plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    img = cv2.imread(data.filepaths[i + len(X_train)])  # Adjust the index to access test set images
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title(f'Pred: {class_labels[y_pred[i]]}')
    plt.axis('off')
plt.show()
