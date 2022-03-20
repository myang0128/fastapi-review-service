FROM registry.access.redhat.com/ubi8/python-39

LABEL maintainer="Mark Curwen<macurwen@redhat.com>"

LABEL io.k8s.description="This is an fastapi app to get the review page" \
      io.k8s.display-name="review"

ENV CONFIGURATION_SETUP=development
ENV PORT 8083
ENV DATA_SERVICE_HOST http://3021d12dc67c.ngrok.io
ENV DATA_SERVICE_PORT 8500

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 8083

ENTRYPOINT [ "python" ]

CMD ["/app/main.py"]