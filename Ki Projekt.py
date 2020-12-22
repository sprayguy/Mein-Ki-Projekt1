pip install pip
pip install --upgrade pip
pip install tensorflow
pip install tf-nightly

docker pull tensorflow/tensorflow:latest #Die bilder
docker run -it -p 8888:8888 tensorflow/tensorflow:latest-jupyter #server starten

import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential ([
    keras.layers.Flatten( input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.  layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam'), loss='sparse_categorical_crossentropy', metrics=
['accuracy']

model.fit(train_images, train_labels, epoche=10)