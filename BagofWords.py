import nltk
nltk.download('brown')
nltk.download('stopwords')
nltk.download('popular')


from nltk.corpus import brown, stopwords
print(brown.words())
print(stopwords.words())

import tensorflow as tf
from tensorflow.keras.layers import MultiHeadAttention, LayerNormalization, Dense

