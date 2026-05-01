# Hotel_Reservation_MLOps-Project

in this stad ( i build the MLOps project locally) => to migrate it into the cloud GCP with CI/CD (with Jenkins)

- download Jenkins Image with Docker ( custom_Jenkins with Dockerfile )
  and Execute `docker build -t jenkins-dind .`
- then if want to execute the docker image : """docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins jenkins-dind"""
  - i named the container `jenkins`
  - for obtain the password make a command `docker logs jenkins` => Jenkins -> represent the name of the container
  - for rerun it with just this command `docker run jenkins` => instead the jenkins , we can put container_name / id
    > for download Google cloud cli
  - execute the bach command of the jenkins : `docker exec -u root -it jenkins bash` ( after this `docker restart jenkins`)
    ,we'll be enter into the root the jenkins container envirement
  - download Google-Cloud-Cli :
    '''
    apt-get update
    apt-get install -y curl ca-certificates gnupg

        curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
        gpg --dearmor -o /usr/share/keyrings/google-cloud.gpg

        echo "deb [signed-by=/usr/share/keyrings/google-cloud.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
        > /etc/apt/sources.list.d/google-cloud-sdk.list

        apt-get update
        apt-get install -y google-cloud-cli
        '''

        then `gcloud --version`=> for checking if installed

  - then `groupadd docker` ( could showed you an error )
  - `usermod -aG docker jenkins` then `usermod -aG root jenkins`
 + enable the services on GCP 
  + Cloud Container Register API
  + Artifact Registry API
  + Cloud Ressource Manager API
+ add role to IAM (for the project_API/name)  => add "owner role"
  i faced an error in my code : 
    1. i changed the name of the image in GCR &&  run => sudo chmod 666 /var/run/docker.sock
    2. sudo usermod -aG docker jenkins => ( depend on image / container name)
       sudo systemctl restart jenkins