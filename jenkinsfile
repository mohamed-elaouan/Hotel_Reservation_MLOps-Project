pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
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
    }
}
