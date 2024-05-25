FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1
ENV CHANNEL=test
ENV USER=user

# Install pip requirements
COPY requirements.txt .


RUN python -m pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/Poland /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
    
WORKDIR /opt/app/
COPY . /opt/app/

CMD ["python", "scripts/observer.py"]
