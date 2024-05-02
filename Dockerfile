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

EXPOSE 8080
ENV PORT 8080

# 
CMD ["uvicorn", "backend_cloud.main:app", "--host", "0.0.0.0", "--port", "8080"]