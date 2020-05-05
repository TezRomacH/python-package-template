FROM python:3.7-slim-buster

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  make \
  && rm -rf /var/lib/apt/lists/*

COPY Makefile .
RUN make download-poetry && make install && rm Makefile

CMD mkdir -p /workspace
WORKDIR /workspace
