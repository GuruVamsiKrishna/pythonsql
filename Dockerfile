FROM python:3

WORKDIR /usr/src/app
ENV host_name pocdb.cyct3n8wcn54.ap-south-1.rds.amazonaws.com #rds end point
ENV user_name admin
ENV pass_name guruvamsi
ENV data_name pets
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python","sql.py" ]
