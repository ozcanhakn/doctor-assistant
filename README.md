# 🩺 Doktor Asistanı - GPT Destekli Terminal & API Projesi

Bu proje, OpenAI destekli bir Doktor Asistanı Chatbot'udur. Kullanıcılar terminalden ya da bir HTTP API üzerinden sağlık sorunlarını yazabilir ve yanıt alabilir.

---

## 🔧 Kurulum

### 1. Bu repoyu klonla
```bash
git clone https://github.com/kullaniciadiniz/doktor-asistani.git
cd doktor-asistani
```

### 2. Sanal ortam oluştur
```python -m venv venv```

### 3. Ortamı aktifleştir

#### Windows için

```venv\Scripts\activate```

#### Mac/Linux için

```source venv/bin/activate```

### 4. Gerekenleri yükle

```pip install -r requirements.txt```

---

## 🔑 Ortam Değişkeni (.env)

Ana dizinde bir .env dosyası oluştur ve içerisine şu satırı ekle:

```OPENAI_API_KEY=senin_openai_anahtarın```

---

## 🚀 Çalıştırma

### 1. Terminal Üzerinden Kullanım

```python doctor_assistant_terminal.py```

### 2. API Sunucusu Başlatma

```uvicorn doctor_assistant_api:app --reload --port 8080```

### 3. API Testi (Terminal İstemcisi)

```python client_test.py```

---

## 🧪 API Endpoint
```POST /chat```

Örnek istek gövdesi:

```
{
  "name": "Hakan",
  "age": 24,
  "message": "şikayetin"
}
```


## 🧠 Kullanılan Teknolojiler

-LangChain

-OpenAI GPT-4

-FastAPI

-Python 3.10+

-dotenv

-requests


## 📂 Proje Yapısı
```bash
project_1/
│
├── doctor_assistant_terminal.py     # Terminal üzerinden sohbet
├── doctor_assistant_api.py          # FastAPI servisi
├── client_test.py                   # API istemcisi
├── requirements.txt                 # Bağımlılıklar
└── .env                             # (Senin oluşturman gereken dosya)
```


## 👤 Geliştirici
[ozcanhakn](https://github.com/ozcanhakn)

