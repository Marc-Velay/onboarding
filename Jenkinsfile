node {
     stage('Build') {
                sh '''
                    ls
                    docker-compose up --build'''

        }
        stage('Test') {
                sh '''
                    docker-compose run web python3 manage.py test'''

        }

    post {
        always {
            sh ''' echo "done" '''
        }
    }
}