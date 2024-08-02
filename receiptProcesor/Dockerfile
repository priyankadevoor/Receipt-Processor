FROM python:3

COPY requirements.txt .
#Install Django and other required packages
RUN pip install -r requirements.txt

# Copy the Django project files into the image
COPY . ./app

# Set the working directory
WORKDIR /app

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]