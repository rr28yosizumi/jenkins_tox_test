pipeline {
    //agent { 
    //    dockerfile {
    //        filename 'Dockerfile'
    //        args '-u root:sudo'
    //    }
    //}
    agent { 
        docker {
            image 'python:3.8'
            args '-u root:sudo'
        } 
    }
    environment {
        PYENV_ROOT = '$HOME/.pyenv'
    }
    stages {
        stage('Test') {
            steps {
                sh 'apt update'
                sh 'apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl'
                sh 'apt install -y git'
                sh 'apt install -y libedit-dev'
                //sh 'wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz'
                //sh 'tar zxvf openssl-1.1.1g.tar.gz'
                //dir('openssl-1.1.1g'){
                //    sh 'ls .'
                //   sh './config --prefix=$HOME/openssl --openssldir=$HOME/openssl no-ssl2'
                //    sh 'make'
                    //sh 'make test'
                //    sh 'make install'
                //    sh 'ls $HOME/openssl/include'
                //    sh 'ls $HOME/openssl/lib'
                //    sh 'ls $HOME/openssl'
                //}
                sh 'git clone https://github.com/pyenv/pyenv.git ~/.pyenv'
                sh '$HOME/.pyenv/bin/pyenv init -'
                sh '$HOME/.pyenv/bin/pyenv install 3.5.9'
                sh '$HOME/.pyenv/bin/pyenv install 3.6.2'
                sh '$HOME/.pyenv/bin/pyenv install 3.7.2'
                sh '$HOME/.pyenv/bin/pyenv install 3.8.2'
                sh 'python -V'
                //sh 'CFLAGS=-I$HOME/openssl/include LDFLAGS=-L$HOME/openssl/lib SSH=$HOME/openssl $HOME/.pyenv/bin/pyenv install 3.7.3'
                //sh 'CFLAGS=-I$HOME/openssl/include LDFLAGS=-L$HOME/openssl/lib SSH=$HOME/openssl $HOME/.pyenv/bin/pyenv install 3.8.2'
                sh 'pip install -r requirements_dev.txt'
                sh 'pip install tox-pyenv'
                sh 'tox'
            }
        }
    }
}