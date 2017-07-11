pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''rm -rf env
                    virtualenv env
                    source env/bin/activate
                    pip install -r requirements.txt'''
            }
        }
        stage('Test') {
            steps {
                sh '''source env/bin/activate
                python manage.py test'''
            }
        }
    }
    post {
        always {
            sh ''' echo "done" '''
        }
    }
}