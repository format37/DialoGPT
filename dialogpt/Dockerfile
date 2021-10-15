#FROM continuumio/miniconda
FROM nvidia/cuda:11.4.2-devel-ubuntu20.04
#WORKDIR /server

COPY requirements.txt /
COPY service.py /

# install miniconda
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh 

# install environment
ADD environment.yml environment.yml

RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/rudialogpt/bin:$PATH
RUN /bin/bash -c "source activate rudialogpt;pip3 install -r requirements.txt --no-cache-dir;python service.py"