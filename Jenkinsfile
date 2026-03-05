pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
        // below is the Project ID of the GCP project that we will be using for this project, you can change it to your own project ID if you want to test the pipeline on your own GCP project
        GCP_PROJECT = 'learningprojects-486111'
        GCLOUD_PATH = "/var/jenkins_home/google-cloud-sdk/bin"
    }

    stages {
        stage('cloning Github repo to Jenkins/after changing Error name') {
            steps {
                script {
                    echo 'Cloning GitHub repo to Jenkins ..........'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/mohamed-elaouan/Hotel_Reservation_MLOps-Project.git']])
                }
            }
        }
        stage('Setting up our virtual environment and installing dependencies') {
            steps {
                script {
                    echo 'Setting up our virtual environment and installing dependencies ..........'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage('Building and pushing our Docker image to GCR') {
            steps {
                withCredentials([file(credentialsId:'gcp-key', variable:'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Building and pushing our Docker image to GCR ..........'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        '''
                    }
                }
            }
        }
    }
}
