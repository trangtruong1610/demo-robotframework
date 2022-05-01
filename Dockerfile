FROM python:3.9.12
COPY docker /demo-robotframework
WORKDIR /demo-robotframework
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null
