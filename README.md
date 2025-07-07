# 🧠 NLP Text Classifier API

Bu proje, basit bir metin sınıflandırması yapabilen FastAPI tabanlı bir RESTful servistir. Örnek olarak olumlu/olumsuz duygu analizi yapar.

## 🚀 Özellikler

- FastAPI ile geliştirilmiş REST API
- `scikit-learn` ile eğitilmiş Naive Bayes model
- Docker desteği ile kolay dağıtım
- Swagger (OpenAPI) dokümantasyonu

## 🧪 Örnek Kullanım

POST isteğiyle sınıflandırma:

```bash
curl -X POST "http://localhost:8000/predict?text=harika"
