ARG IMAGE_VERSION
FROM $IMAGE_VERSION

RUN apt-get update && DEBIAN_FRONTEND=noninteractive && apt-get install -y \
    python3 \
    python3-pip

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
