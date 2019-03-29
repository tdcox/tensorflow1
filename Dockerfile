FROM python:onbuild
COPY requirements.txt .
ENV PORT 8080
EXPOSE 8080
RUN pip install tensorflow
ENTRYPOINT ["python"]
CMD ["app.py"]
