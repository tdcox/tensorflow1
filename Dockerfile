FROM tensorflow/tensorflow:latest-py3
WORKDIR /usr/src/app
COPY requirements.txt .
ENV PORT 8080
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]
