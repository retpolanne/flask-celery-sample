FROM python:3.7.6-alpine3.11

COPY . /src/app
WORKDIR /src/app
RUN apk add build-base make gcc linux-headers pcre-dev && make install
RUN make test
