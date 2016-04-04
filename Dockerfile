FROM vamiko/project
MAINTAINER Myroslav Stefaniuk
RUN apt-get install curl libcurl3 libcurl3-dev -y
RUN apt-get update
RUN apt-get build-dep python-imaging -y
RUN apt-get install libjpeg62 libjpeg62-dev -y
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
WORKDIR /project
EXPOSE 80