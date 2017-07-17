pipeline {
     agent any

     stages {
        stage('Build') {
            steps {
                sh '''
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