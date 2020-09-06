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
                sh 'apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl'
                sh 'apt install -y git'
                sh 'apt install -y libedit-dev'
                sh 'git clone https://github.com/pyenv/pyenv.git ~/.pyenv'
                sh '$HOME/.pyenv/bin/pyenv init -'
                sh '$HOME/.pyenv/bin/pyenv install 3.5.9'
                sh '$HOME/.pyenv/bin/pyenv install 3.6.2'
                sh 'CFLAGS=-I$HOME/openssl/include LDFLAGS=-L$HOME/openssl/lib SSH=$HOME/openssl $HOME/.pyenv/bin/pyenv install 3.7.3'
                sh 'CFLAGS=-I$HOME/openssl/include LDFLAGS=-L$HOME/openssl/lib SSH=$HOME/openssl $HOME/.pyenv/bin/pyenv install 3.8.2'
                sh 'pip install -r requirements_dev.txt'
                sh 'tox'
            }
        }
    }
}