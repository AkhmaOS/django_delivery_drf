FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN apt update -y && apt install -y \
    binutils \
    libproj-dev \
    gdal-bin


WORKDIR /opt/tuteda/server

RUN pip install -U pip setuptools wheel \
    django==2.2.3 \
    django-admin-sortable2==0.7.2 \
    django-allauth==0.39.1 \
    django-ckeditor==5.7.1 \
    django-debug-toolbar==2.0 \
    django-filter==2.2.0 \
    django-rest-auth==0.9.5 \
    djangorestframework==3.9.4 \
    django-map-widgets==0.2.2 \
    pillow==6.1.0 \
    psycopg2-binary==2.8.3 \
    sentry-sdk==0.10.2 \
    sorl-thumbnail==12.5.0 \
    uwsgi==2.0.18\
    django-colorfield\
    django-phonenumber-field[phonenumbers]\
    django-filer

COPY . .

RUN chmod +x "./entrypoint.sh"
ENTRYPOINT ["sh", "./entrypoint.sh"]

EXPOSE 8000
ENV PORT 8000

CMD ["uwsgi", "./tuteda/uwsgi.ini"]
