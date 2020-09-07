FROM tiangolo/uwsgi-nginx:python3.8

COPY config/requirements.pip /requirements.pip

RUN pip install -r /requirements.pip

ENV STATIC_URL /static
ENV STATIC_PATH /app/static
ENV STATIC_INDEX 0

COPY ./app /app
WORKDIR /app

ENV PYTHONPATH=/app

RUN mv /entrypoint.sh /uwsgi-nginx-entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME ["/notes"]

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/start.sh"]
