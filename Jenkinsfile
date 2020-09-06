pipeline {
    //agent { dockerfile true }
    agent { 
        docker {image 'python:3.6.2'} 
    }
    stages {
        stage('Test') {
            steps {
                sh 'pip install -r requirements_dev.txt'
                sh 'tox'
            }
        }
    }
}