node {
     stage('Build') {
                sh '''
                    rm -rf ./*
                    git pull remote https://github.com/Marc-Velay/onboarding
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