"""Number Recognizer."""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def plot_images(images, labels):
    """."""
    n_cols = min(5, len(images))
    n_rows = len(images) // n_cols
    fig = plt.figure(figsize=(8, 8))

    for i in range(n_cols * n_rows):
        sp = fig.add_subplot(n_rows, n_cols, i + 1)
        plt.axis('off')
        plt.imshow(images[i], cmap='gray')
        sp.set_title(labels[i])
    plt.show()


mnist = fetch_openml('mnist_784')
X = mnist['data'][:10000, :]
y = mnist['target'][:10000]

print(X.shape)
print(y.shape)

y = y.astype("int32")
X = X / 255

train_X, test_X, train_y, test_y = train_test_split(X, y)

clf = MultinomialNB()
clf.fit(train_X, train_y)

predictions = clf.predict(test_X)

p = np.random.permutation(len(test_X))
p = p[:20]
plot_images(test_X[p].reshape(-1, 28, 28), predictions[p])
