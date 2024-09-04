import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score


def generate_synthetic_data(num_samples=1000, sequence_length=30, image_shape=(64, 64, 1), num_classes=10):
    X = np.random.rand(num_samples, sequence_length, *image_shape)
    y = np.random.randint(num_classes, size=(num_samples,))
    return X, y


X, y = generate_synthetic_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = models.Sequential()


model.add(layers.TimeDistributed(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(None, 64, 64, 1))))
model.add(layers.TimeDistributed(layers.MaxPooling2D((2, 2))))
model.add(layers.TimeDistributed(layers.Conv2D(64, (3, 3), activation='relu')))
model.add(layers.TimeDistributed(layers.MaxPooling2D((2, 2))))
model.add(layers.TimeDistributed(layers.Flatten()))


model.add(layers.LSTM(128))


model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))  


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))


y_pred = np.argmax(model.predict(X_test), axis=-1)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))


import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'], label='train_accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
