FROM python:3
ADD . /.
RUN python3 setup.py
CMD ["python3", "setup.py","index.py"]