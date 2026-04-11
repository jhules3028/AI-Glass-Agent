FROM ubuntu:latest
LABEL authors="jules"

ENTRYPOINT ["top", "-b"]