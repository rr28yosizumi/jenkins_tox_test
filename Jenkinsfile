pipeline {
    //agent { dockerfile true }
    agent { 
        docker {image 'python:3.6.2'} 
    }
    stages {
        stage('Test') {
            steps {
                sh 'python setup.py test'
            }
        }
    }
}