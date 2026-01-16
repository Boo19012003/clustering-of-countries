# Hướng dẫn cài đặt và chạy

Yêu cầu:

- Python 3.13.9

Các bước:

1. Tạo và kích hoạt virtual environment (tuỳ OS):

```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Cài đặt phụ thuộc:

```
pip install --upgrade pip
pip install -r requirements.txt
```

3. Chạy ứng dụng Streamlit:

```
streamlit run app.py
```

Ghi chú:

- File chính: `app.py`
- Nếu gặp lỗi liên quan đến phiên bản, thử nâng/cố định phiên bản trong `requirements.txt`.
