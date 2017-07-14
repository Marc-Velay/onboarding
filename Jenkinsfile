pipeline {
     agent any

     stages {
        stage('Build') {
            steps {
                sh '''
                    apt-get install python3-pip
                    pip install virtualenv
                    rm -rf env
                    virtualenv --python=python3.5 env
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