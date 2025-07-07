import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Basit eğitim verisi
data = {
    "text": ["iyi film", "kötü film", "harika", "berbat", "mükemmel", "vasat"],
    "label": [1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Metinleri sayısal verilere dönüştür
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

# Modeli eğit
model = MultinomialNB()
model.fit(X, df["label"])

# Model ve vectorizer'ı dosyaya kaydet
with open("model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)
