# Receipt-Processor

The application is built using Django framework and the api endpoints can be seen in views.py.
The application is containerized using docker and the image is pushed to the Docker Hub.
In order to run the application follow the below steps - 
1. Open docker application.
2. In a terminal pull the docker image using command - docker pull priyadevoor/django-docker:latest
3. Now run the image using the command - docker run -p 8000:8000 priyadevoor/django-docker:latest


![image](https://github.com/user-attachments/assets/326d54b7-3c0a-4715-b08c-749ca434142d)

The docker image is running and it will host the application in localhost in port 8000. Open it in any web browser and the below page will be visible.

![image](https://github.com/user-attachments/assets/4052278f-7799-419f-bea2-4fae04d734cb)

go to the endpoint /receipts/process, a page will open where you can give the input in JSON format and POST.

![image](https://github.com/user-attachments/assets/d439a5a6-d0e7-4243-94dc-c682991ed4d4)

If the post request was success id will be returned.

![image](https://github.com/user-attachments/assets/1c1e3bed-0bff-4a30-b7d8-cb941eca37c9)

Go to endpoint /receipts/<id>/points, to get the points.

![image](https://github.com/user-attachments/assets/fcb7a84e-11b5-4469-877a-a3bb850026b3)




