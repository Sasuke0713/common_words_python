FROM python:3.9-alpine

RUN apk add build-base
RUN adduser --system --disabled-password --home /home/app app
WORKDIR /home/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./common_word_sequences.py", "example.txt" ]
