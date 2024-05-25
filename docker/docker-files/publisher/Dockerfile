FROM python:3.10
ENTRYPOINT [ "docker/docker-files/generator/cleanup.sh" ]
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY docker/docker-files/generator/requirements.txt .


RUN python -m pip install -r requirements.txt


RUN apt-get update && \
    apt-get install -yq tzdata ca-certificates curl gnupg sudo && \
    ln -fs /usr/share/zoneinfo/Poland /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
        
# WORKDIR /scripts
WORKDIR /opt/app/
COPY . /opt/app/

CMD ["python", "scripts/publisher.py"]
