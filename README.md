# Hotel_Reservation_MLOps-Project

in this stad ( i build the MLOps project locally) => to migrate it into the cloud GCP with CI/CD (with Jenkins)

- download Jenkins Image with Docker ( custom_Jenkins with Dockerfile )
  and Execute `docker build -t jenkins-dind .`
- then if want to execute the docker image : """docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v 
                                                /var/run/docker.sock:/var/run/docker.sock --name jenkins jenkins-dind"""
    + i named the container `jenkins`
    + for obtain the password make a command `docker logs jenkins` => Jenkins -> represent the name of the container
