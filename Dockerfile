FROM vamiko/project
MAINTAINER Myroslav Stefaniuk
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get install curl libcurl3 libcurl3-dev -y
WORKDIR /project
EXPOSE 80