import numpy as np

words = np.array([
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli fruit", "vanilla", "watermelon", "xigua", "yellow", "passion", "fruit", "zucchini"
])

def get_random_word():
    word = np.random.choice(words)
    return word

