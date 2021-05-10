title: Customizing MobileNetV2 through transfer learning

[TOC]


## Customizing MobileNetV2

In [the previous tutorial](%link:image-classification%), you learned how to use MobileNetV2, a pretrained network for image classification. This is fun, but there are not many situations in which you want to perform the exact same task that MobileNetV2 has been trained on.

Therefore, in this tutorial, you will learn how to modify and retrain MobileNetV2 to perform another task than the one it was trained on: distinguishing male and female cats. This is an example of *transfer learning*: using the fact that having already learned one task (image classification using a 1000 categories) makes it easier to learn another task (distinguishing male and female cats).


## Importing MobileNetV2

We again start by loading MobileNetV2.

```python
from keras.applications.mobilenet_v2 import MobileNetV2

model = MobileNetV2(weights='imagenet')
```


## Loading images and creating labels

Our training data consists of 40 images: twenty pictures of male cats and twenty pictures of female cats. These pictures are taken from [this online experiment](http://www.chrislongmore.co.uk/experiments/catfaces/) by Chris Longmore. You can download the images [here](/data/cats.zip).

We first create an empty array of shape `(40, 224, 224, 3)`. This corresponds to 40 images of 224 × 224 pixels with three color channels.

```python
import numpy as np

data = np.empty((40, 224, 224, 3))
```

I extracted the images to a subfolder called `data/cats`. The files are called `f01.jpg`, `f02.jpg` … `f20.jpg` for the female cats, and `m01.jpg` … `m20.jpg` for the male cats.

%--
figure:
    source: f06.jpg
    id: FigFemaleCat
    caption: A female cat.
--%

%--
figure:
    source: m10.jpg
    id: FigMaleCat
    caption: A male cat.
--%

We first read in the female cats, and put them in the first 20 places of the `data` array. Each image is first read, then preprocessed so that the pixel values are in the -1 to 1 range, then resized to 224 × 224, and finally assigned to the `data` array. (See [this previous tutorial](%link:image-classification%) if you're unsure how this works.)

```python
from imageio import imread
from skimage.transform import resize
from keras.applications.mobilenet_v2 import preprocess_input

for i in range(0, 20):
    im = imread('data/cats/f{:02d}.jpg'.format(i + 1))
    im = preprocess_input(im)
    im = resize(im, output_shape=(224, 224))
    data[i] = im
```

Next we read in the male cats, and put them in the last 20 places of the `data` array:

```python
for i in range(0, 20):
    im = imread('data/cats/m{:02d}.jpg'.format(i + 1))
    im = preprocess_input(im)
    im = resize(im, output_shape=(224, 224))
    data[i + 20] = im
```

The training labels correspond to an array of length 40, where the first 20 values are 0 and the last 20 values are 1. In other words, we code the female cats as category 0 and the male cats as category 1.

```python
labels = np.empty(40, dtype=int)
labels[:20] = 0
labels[20:] = 1
```


## Checking if our cats are recognized as cats

Although MobileNetV2 has not (yet) been trained to distinguish male and female cats, it *has* been trained to recognize cats in general. Therefore, as a sanity check, let's see whether MobileNetV2 indeed categorizes all of our 40 input images as cats. We only get the top prediction for each image. (See [this previous tutorial](%link:image-classification%) if you're unsure how this works.)

```python
from keras.applications.mobilenet_v2 import decode_predictions

predictions = model.predict(data)
for decoded_prediction in decode_predictions(predictions, top=1):
    for name, desc, score in decoded_prediction:
        print('- {} ({:.2f}%%)'.format(desc, 100 * score))
```

Great! MobileNetV2 has recognized every image as being a cat, and has even identified specific cat breeds. The scores are fairly low, but this is because MobileNetV2 is often unsure about the exact breed, so that the scores are distributed across a few different cat breeds.


## Modifying the model

MobileNetV2 has an output layer that consists of 1000 neurons, which correspond to the 1000 categories that it has been trained on. But here we want to only classify two categories: male and female cats. Therefore, we need an output layer that consists of only two neurons.

We first create a densely connected layer that we will use as our output layer:

```python
from keras.layers import Dense

cat_output = Dense(2, activation='softmax')
```

Next, we connect this output layer to the second-to-last layer of MobileNetV2; that is, we skip the original output layer, and connect our own output layer (`cat_output`) to the rest of the network.

To do this, we first get the output of second-to-last layer (`model.layers[-2].output`), and then call `cat_output` as if it's a function and pass this output as an argument. The return value is a special kind of object (a `KerasTensor`).

```python
cat_output = cat_output(model.layers[-2].output)
```

(Side note: Here we are using Keras's so-called [functional programming style](https://keras.io/guides/functional_api/). This is less user-friendly than the [sequential programming style](https://keras.io/guides/sequential_model/) that we used in previous tutorials, but it has the advantage of being more flexible; for example, the functional programming style allows you to construct complex, non-linear network architectures. And importantly: if you want to work with a model, such as MobileNetV2, that has been built using the functional programming style, then you have no choice but to use this style as well.)

Next we create a new model, using the `Model` class. `Model()` requires two arguments: `inputs`, for which we simply use the input object from the original model; and `outputs`, which is our newly created output object. (Technically, both of these objects are `KerasTensor`s.)

```python
from keras import Model

cat_input = model.input
cat_model = Model(inputs=cat_input, outputs=cat_output)
```

Our `cat_model` contains 156 layers with about 2.2 million parameters. It takes a lot of time and data to train a model of this size. Fortunately, the model has already been trained for the most part, because we have simply copied all layers except for the output layer from MobileNetV2. Therefore, and to the extent that the original training is useful for our new purpose, we don't need to train these layers again, and we can *freeze* them.

To freeze a layer, simply set its `trainable` property to `False`. We do this for all layers except the last one, which is our newly created output layer.

```python
for layer in cat_model.layers[:-1]:
    layer.trainable = False
```

Our cat model is now ready to be compiled. (See [this previous tutorial](%link:basics%) if you're unsure how this works.)

```python
cat_model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```


## Training the modified model

Ok, let's now train our cat model to distinguish male and female cats. (See [this previous tutorial](%link:basics%) if you're unsure how this works.)

```python
cat_model.fit(x=data, y=labels, epochs=20, verbose=2)
```

Wow! The accuracy converges on 1, which suggests that the model is indeed able to distinguish male and female cats. This is surprising given that (to me) they look very similar.

We can verify the accuracy by generating predictions for the training data, using `np.argmax()` to decode the predictions into female (0) or male (1). (See [this previous tutorial](%link:basics%) if you're unsure how this works.)

```python
predictions = cat_model.predict(data)
print('Should be female (0)')
print(np.argmax(predictions[:20], axis=1))
print('Should be male (1)')
print(np.argmax(predictions[20:], axis=1))
```

100% accurate! Does this mean that our cat model is really able to distinguish male and female cats?


## Validating model performance with separate validation data

… Not necessarily.

So far, we've only seen how well the model is able to classify images that were part of the training data. The real test is whether the model is also able to classify images that it hasn't seen before.

In other words: we need a separate dataset for validation. One way to do this is by splitting the original data into two sets, one consisting of training data (30 images) and one consisting of validation data (10 images). And we then test how well the model is able to classify the validation data after having been trained only on the training data.

Let's first create two new datasets, `training_data` and `validation_data`, as well as their corresponding labels, `training_labels` and `validation_labels`.


```python
# The first 15 images for male and female cats will be used for training
training_data = np.empty((30, 224, 224, 3))
training_data[:15] = data[:15]
training_data[15:] = data[20:35]
training_labels = np.empty(30)
training_labels[:15] = 0
training_labels[15:] = 1
# The last 5 images for male and female cats will be used for validation
validation_data = np.empty((10, 224, 224, 3))
validation_data[:5] = data[15:20]
validation_data[5:] = data[35:]
validation_labels = np.empty(10)
validation_labels[:5] = 0
validation_labels[5:] = 1
```

We create a fresh cat model (`cat_model2`) that is identical to our previous cat model, except that we haven't retrained it yet.

```python
cat_output2 = Dense(2, activation='softmax')
cat_output2 = cat_output2(model.layers[-2].output)
cat_input2 = model.input
cat_model2 = Model(inputs=cat_input2, outputs=cat_output2)
for layer in cat_model2.layers[:-1]:
    layer.trainable = False
cat_model2.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

We then retrain our fresh cat model, just as before, except that this time we use the `validation_data` keyword to pass our validation data and labels as a `tuple`.

```python
cat_model2.fit(
    x=training_data,
    y=training_labels,
    validation_data=(validation_data, validation_labels),
    epochs=20,
    verbose=2
)
```

As before, the (regular) accuracy goes up to 1. But crucially, the validation accuracy does not! This means that our model never really learned to distinguish male and female cats; it merely learned to recognize all of the exemplars that we trained it on, without being able to generalize this knowledge to new cats. This is called *overfitting* and often happens when a network is trained with a small dataset and/ or on a difficult task. (Both of which are true here.)

It's just really hard to tell apart male cat from female cats. That's also what Chris Longmore concluded.


## Video tutorial

%--
video:
    id: VidTutorial
    source: youtube
    videoid: 8LjK4knsTRQ
    caption: Watch this tutorial on YouTube!
--%
