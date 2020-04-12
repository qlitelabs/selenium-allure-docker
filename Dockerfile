FROM python:slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src .
CMD ["python", "-m", "pytest", "--alluredir=reports/allure-reports"]