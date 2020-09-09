pipeline {
    agent { 
        dockerfile {
            filename 'Dockerfile'
            args '-u root:sudo'
        }
    }
    stages {
        stage('setup') {
            steps {
                sh 'pip install flake8'
                sh 'pip install tox'
                sh 'pip install tox-pyenv'
            }
        }
        stage('test') {
            steps {
                sh 'tox'
                // カバレッジを取得
                cobertura coberturaReportFile: 'coverage.xml'
                // テスト結果を取得　
                junit 'junit_reports/*.xml'
            }
        }
    }
}