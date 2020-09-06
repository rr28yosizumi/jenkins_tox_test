pipeline {
    //agent { dockerfile true }
    agent { 
        docker {
            image 'python:3.6.2'
            args '-u root:sudo'
            } 
    }
    stages {
        stage('Test') {
            steps {
                sh 'apt update'
                sh 'apt install -y gcc make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libedit-dev'
                sh 'apt install -y git'
                sh 'git clone https://github.com/pyenv/pyenv.git ~/.pyenv'
                sh '$HOME/.pyenv/bin/pyenv init -'
                sh '$HOME/.pyenv/bin/pyenv install 3.5.9'
                sh '$HOME/.pyenv/bin/pyenv install 3.6.2'
                sh 'CFLAGS=-I/usr/include/openssl LDFLAGS=-L/usr/lib $HOME/.pyenv/bin/pyenv install 3.7.3'
                sh 'CFLAGS=-I/usr/include/openssl LDFLAGS=-L/usr/lib $HOME/.pyenv/bin/pyenv install 3.8.2'
                sh 'pip install -r requirements_dev.txt'
                sh 'tox'
            }
        }
    }
}