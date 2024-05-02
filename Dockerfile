# 
FROM python:3.11.8

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY . ./backend_cloud

# 
CMD ["uvicorn", "backend_cloud.main:app", "--host", "0.0.0.0", "--port", "80"]