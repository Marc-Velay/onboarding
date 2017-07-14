pipeline {
     agent any

     stages {
        stage('Build') {
            steps {
                sh '''
                    pip3 install virtualenv
                    rm -rf env
                    virtualenv env
                    source env/bin/activate
                    python -V
                    pip3 install docker-compose
                    ls
                    docker build -t localhost:9999/django-app .'''
            }
        }
    }
    post {
        always {
            sh ''' echo "done" '''
        }
    }
}