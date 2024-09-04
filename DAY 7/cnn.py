import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds


dataset, info = tfds.load('tf_flowers', as_supervised=True, with_info=True, split=['train[:80%]', 'train[80%:]'])
train_dataset, test_dataset = dataset


def preprocess(image, label):
    image = tf.image.resize(image, (128, 128))
    image = image / 255.0  
    return image, label

batch_size = 32

train_dataset = train_dataset.map(preprocess).shuffle(1000).batch(batch_size)
test_dataset = test_dataset.map(preprocess).batch(batch_size)


model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(5, activation='softmax')  
])


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


history = model.fit(train_dataset, epochs=10, validation_data=test_dataset)


test_loss, test_acc = model.evaluate(test_dataset)
print(f"Test accuracy: {test_acc}")


plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

for images, labels in test_dataset.take(1):
    predictions = model.predict(images)
    predicted_labels = tf.argmax(predictions, axis=1)

    plt.figure(figsize=(10, 10))
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy())
        plt.title(f"True: {labels[i].numpy()}, Pred: {predicted_labels[i].numpy()}")
        plt.axis('off')
    plt.show()
