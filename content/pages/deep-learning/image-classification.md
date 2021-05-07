title: Classifying images with MobileNetV2
next_title: Transfer learning
next_url: %url:transfer-learning%

[TOC]


## MobileNetV2

Keras includes a number of pretrained networks ('applications') that you can download and use straight away. One of these is [MobileNetV2](https://keras.io/api/applications/mobilenet/), which has been trained to classify images.

You can simply import `MobileNetV2` from `keras.applications` and create an instance of it. The first time that you do this, the network will be downloaded from the internet.

If you don't pass any keywords to `MobileNetV2()`, then the network will have random weights; that is, you will get the architecture of the network, but not the weights, and you will therefore have to train it yourself. By specifying `weights='imagenet'`, you indicate that you want the network to be pretrained.

```python
from keras.applications import MobileNetV2

model = MobileNetV2(weights='imagenet')
# model.summary()  # Uncomment this to print a long summary!
```


## Preparing an image for model input

We're going to ask MobileNetV2 to which category the following image belongs:

%--
figure:
    source: boef.jpg
    id: FigBoef
    caption: |
        The Boef on her birthday.
--%

This is a photo of The Boef when she was celebrating her birthday at my mother's place, where it seems that things escalated. The Boef is a bunny, but to a naive observer this may not be obvious. So it's interesting to see what MobileNetV2 sees in this photo.

Neural networks are picky when it comes to the kind of input that they expect. If you provide input in a format that the network doesn't expect, then the predictions won't make sense (if the structure of the input is superficially compatible with the network) or the code will simply crash (if the structure of the input is incompatible).

MobileNetV2 expects images of 224 × 224 pixels with three color channels. In other words, it expects input of shape `(224, 224, 3)`. You can pass multiple images at once to the model, just like we passed multiple numbers to our model in [the previous tutorial](%link:basics%). This means that the input should actually consist of four dimensions, where the first dimension corresponds to the index of the image.

Here we only pass a single image to the model, which means that the first dimension of the input is of size 1.

```python
import numpy as np
from imageio import imread

data = np.empty((1, 224, 224, 3))
data[0] = imread('data/boef.jpg')
```

When you load an image with `imread()`, the pixel values are in the 0 - 255 range. However, MobileNetV2 expects pixel values to be in the -1 to 1 range. You could perform this transformation yourself, but Keras also provides preprocessing functions:

```python
from keras.applications.mobilenet import preprocess_input

data = preprocess_input(data)
```


## Classifying an image

Now that our image is in the correct format for MobileNetV2, we can get the predictions. (See [this previous tutorial](%link:basics%) if you're unsure how this works.)

```python
predictions = model.predict(data)
print('Shape: {}'.format(predictions.shape))
```

As before, the predictions are returned as a two-dimensional array where the first axis corresponds to the observations (images, in this case). Since we have fed only a single image into the model, the first dimension is of size 1. The second axis corresponds to the output neurons of the model. Since MobileNetV2 has 1000 neurons in the output layer, the second dimension is of size 1000.

We can check which output neuron was most active using `np.argmax()`, which provides the index of the highest value:

```python
output_neuron = np.argmax(predictions[0])
print('Most active neuron: {} ({:.2f}%)'.format(
    output_neuron,
    100 * predictions[0][output_neuron]
))
```

However, knowing that neuron 155 became the most active in response to the image of The Boef is not, by itself, very informative, because we also need to know which category this corresponds to. Fortunately, Keras provides a function that automatically maps predictions onto scores for the corresponding categories:

```python
from keras.applications.mobilenet import decode_predictions

for name, desc, score in decode_predictions(predictions)[0]:
    print('- {} ({:.2f}%%)'.format(desc, 100 * score))
```

So MobileNetV2 is fairly confident that The Boef is a Shih-Tzu. Fair enough, MobileNetV2.

%--
figure:
    source: shih-tzu.png
    id: FigShihTzu
    caption: |
        A Shih-Tzu.
--%
