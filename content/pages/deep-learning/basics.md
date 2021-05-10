title: Building a basic neural network
next_title: Classifying images
next_url: %url:image-classification%


[TOC]


## A simple task for a simple model

Our first artificial neural network will be simple, and it therefore needs a simple task to be trained on. We will train it to classify numbers between 0 and 1 as being either less than 0.5 (category 0) or equal to, or higher than, 0.5 (category 1). Phrased differently, we're going to teach the network to round numbers between 0 and 1.


## Generating the data

We first generate an array of 10,000 random numbers (between 0 and 1), which we will use as the training data (or: input) for the model; that is, each training observation consists of a single number. 

`np.random.random(10000)` returns a one-dimensional array of shape `(10000,)`. However, we need a two-dimensional array for our model. Specifically, the first axis should correspond to the individual observations, and should therefore be of length 10,000. The second axis should correspond to the values from each individual observation, and should therefore be of length 1. We can accomplish this by explicitly changing the shape of `data` to `(10000, 1)`.

```python
import numpy as np

data = np.random.random(10000)
data.shape = 10000, 1
print(data[:5])  # Look at the first five observations
```

Next, we check which numbers in the training data are larger than, or equal to, 0.5. This results in an array of boolean values (`True` or `False`), which we turn into an array of `int` (`1` or `0`) values. This array will serve as the labels (or: expected output) for our model.

```python
labels = np.array(data >= .5, dtype=int)
print(labels[:5])  # Look at the first five labels
```


## Building a simple model

The [`Sequential` model class](https://keras.io/guides/sequential_model/) allows you to specify a model's architecture as a `list` (or: sequence, hence the name) of layers. We specify two layers, both of which are `Dense`, which means that each neuron in the layer is connected to all neurons in the layer above.


The first (non-input) layer, which consists of 8 neurons, specifies the shape of the input observations, which in our case is only a single number (i.e., an array of shape `(1, )`). The `activation` keyword specifies how the neurons translate their input to an output. Here we use the rectified-linear-unit function ('relu'), which essentially means that neurons cannot have a negative output.

The second layer, which consists of two neurons, is our output layer. The 'softmax' activation function essentially means that the neuron's output is squashed into the 0 - 1 range.

%--
figure:
    source: perceptron.png
    id: FigPerceptron
    caption: |
        Our network consists of an input layer, a hidden layer, and an output layer.
--%

It is common to think of the input as a layer as well, even though it is not specified as such in Keras. We can therefore think of our model as a three-layer network, with one input layer (consisting of one neuron), one hidden layer (consisting of eight neurons), and one output layer (consisting of two neurons). A layer is referred to as 'hidden' if it's neither an input layer nor an output layer.


```python
from keras import Sequential
from keras.layers import Dense

model = Sequential([
    Dense(units=8, input_shape=(1,), activation='relu'),
    Dense(units=2, activation='softmax'),
])
```

Next, we compile the model so that it's ready to be trained. In doing so, we need to specify three things.

The `optimizer` keyword specifies the algorithm that will be used to adjust the weights in the model. We will use [Adam](https://keras.io/api/optimizers/adam/), but other algorithms are available as well, and the choice of one algorithm over another is largely one of preference and experience.

The `loss` keyword specifies the loss function, which is the algorithm that determines how wrong the model's predictions are. The goal of training is to reduce the loss. We will use [sparse categorical crossentropy](https://keras.io/api/losses/probabilistic_losses/), which assumes that label values of 0 mean that the first neuron in the output layer should be the most active, whereas label values of 1 mean that the second neuron should be the most active.

The `accuracy` keyword specifies a metric that is printed during training so that you have some idea of how well the model is performing. This is just for visualization and doesn't affect the training process itself.

```python
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

Now let's look at the model summary:


```python
model.summary()
```

Our model has 34 parameters, which correspond to all the weights of the connections between the neurons, as well as the bias parameter for each neuron (a kind of baseline level of activity that a neuron has in the absence of any input). 

The first layer consists of eight neurons, which each have one connection to the input neuron plus one bias, so 8 × (1 + 1) = 16 parameters in total. The second layer consists of two neurons, which each have one connection all eight neurons in the preceding layer plus one bias, so 2 × (8 + 1) = 18 parameters in total.


## Training the model

To train the model, we simply call the `fit()` function. During training, the model's 34 parameters are adjusted to minimize the loss.

The `epochs` keyword specifies how often the training data should be used to fit the model. In our case, we specify 10 epochs, which is similar to calling `fit()` 10 times in a row with the same data and labels.

The `verbose` keyword specifies how much information should be printed out during training.

```python
model.fit(x=data, y=labels, epochs=10, verbose=2)
```

As you can see, during training, the loss goes down while the accuracy goes up until it reaches almost 100%. This means that the model has learned our simple task!


## Testing the model

The true test of our model's performance is whether it is able to classify numbers that it wasn't trained on. In our case, we trained the model on no less than 10,000 randomly selected numbers, which means that our model has seen pretty much every number there is to see in the 0 - 1 range. Nevertheless, it is good practice to create a separate test set. So let's create a new array consisting of ten numbers:


```python
test_set = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
```

Now let's look at the model's predictions for our test set:

```python
predictions = model.predict(test_set)
print(predictions)
```

What are we looking at here? The predictions are a 10 by 2 array, where the first axis corresponds to each of our ten test observations, and the second axis refers to the activity of the two neurons in the output layer.

The predictions are easier to interpret if we look at which of the two neurons was most active for each of the ten test observations. We can do this using `np.argmax()` which returns the index of the highest element in the array.

```python
print(np.argmax(predictions, axis=1))
```

Now we can easily tell that for the first five test observations (0, 0.1, 0.2, 0.3, 0.4), the first output neuron (0) was most active. This means that the network correctly classified these numbers as being less than 0.5. For the last five test observations (0.5, 0.6, 0.7, 0.8, 0.9), the second output neuron (1) was most active. This again means that the network correctly classified these numbers, this time as being equal to, or larger than, 0.5.


## Validating the model during training

As mentioned above, it's important to verify a model's predictions using data that the model wasn't actually trained on. This is important because models are prone to *overfitting*, which occurs when a model has learned the specifics of the training data but is still unable to make (correct) predictions for new observations.

We will look at this in more detail in [a later tutorial](%link:transfer-learning%), but for now let's introduce the concept of *validation data*. By specifying the `validation_split` keyword, we can tell the model to set apart some of the data (10% in the example blow) as validation data. This data will not be used for training, and you will see a separate accuracy metric (`val_accuracy`) for this subset of the data.

We need to start with a fresh, untrained model. So let's first create a new model, copying the code above:

```python
model = Sequential([
    Dense(units=8, input_shape=(1,), activation='relu'),
    Dense(units=2, activation='softmax'),
])
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
```

And now train our fresh model, this time setting 10% of the data apart for validation!

```python
model.fit(x=data, y=labels, epochs=10, verbose=2, validation_split=.1)
```

In this case, the validation accuracy is just as high as the regular accuracy, which means that our model does not suffer from overfitting!


## Video tutorial

%--
video:
    id: VidTutorial
    source: youtube
    videoid: XBc3kbel7XY
    caption: Watch this tutorial on YouTube!
--%
