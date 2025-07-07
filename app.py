from fastapi import FastAPI
import pickle

app = FastAPI()

# Model ve vectorizer'ı yükle
with open("model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

@app.get("/")
def root():
    return {"message": "nlp-text-classifier API çalışıyor."}

@app.post("/predict")
def predict(text: str):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return {"text": text, "prediction": int(prediction)}
