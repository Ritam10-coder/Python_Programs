import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
data_dir = 'path_to_your_flower_dataset'  
datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
batch_size = 32
image_size = (224, 224)
data = datagen.flow_from_directory(data_dir, target_size=image_size, batch_size=batch_size, class_mode='categorical', shuffle=False)
class_labels = list(data.class_indices.keys())
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
features = base_model.predict(data)
features = features.reshape(features.shape[0], -1)  # Flatten the features
le = LabelEncoder()
labels = le.fit_transform(data.classes)
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
svm_classifier = SVC(kernel='linear', C=1.0)
svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred, target_names=class_labels))
print("Accuracy Score:", accuracy_score(y_test, y_pred))
import matplotlib.pyplot as plt
import cv2
plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    img = cv2.imread(data.filepaths[i + len(X_train)])  
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title(f'Pred: {class_labels[y_pred[i]]}')
    plt.axis('off')
plt.show()
