FROM python:3.9-slim 
#çalışacak olduğum base image dosyasını aldım

WORKDIR /app
#çalışma dizinimi belirledim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#requirements.txt dosyasını kopyaladım ve gerekli kütüphaneleri yükledim, indirilen dosyaları local cache eklemedim.

COPY . .
#uygulama dosyalarımı kopyaladım

RUN python manage.py collectstatic --noinput
#static dosyalarımı topladım

CMD ["gunicorn", "mainapp.wsgi:application", "--bind", "0.0.0.0:8000"]
#uygulamamı çalıştırmak için gunicorn kullandım ve 8000 portunda çalıştırdım