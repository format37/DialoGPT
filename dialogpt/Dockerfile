FROM nvidia/cuda:11.4.2-devel-ubuntu20.04
#WORKDIR /server

#EXPOSE 8083
RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip -y
RUN pip3 install --upgrade pip
COPY requirements.txt /
RUN pip3 install -r requirements.txt --no-cache-dir
COPY service.py /

ENTRYPOINT ["python3"]
CMD ["service.py"]