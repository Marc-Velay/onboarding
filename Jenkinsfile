pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''rm -rf env
                    virtualenv env
                    source env/bin/activate
                    pip3 install -r requirements.txt
                    python3 manage.py migrate'''
            }
        }
        stage('Test') {
            steps {
                sh '''source env/bin/activate
                python3 manage.py test'''
            }
        }
    }
    post {
        always {
            sh ''' echo "done" '''
        }
    }
}