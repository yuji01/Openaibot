FROM rust:1.67-slim AS builder
ENV WORKDIR /app
WORKDIR $WORKDIR
ADD . $WORKDIR
RUN apt update && apt install build-essential git curl python3-pip python3-dev ffmpeg -y 
RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir -r requirements.txt
