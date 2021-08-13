pipeline {
  environment {
    GITHUB_TOKEN = credentials('github-token')
  }
  agent {
    docker {
      image "python:latest"
      label "first-vm"
    }
  }
  stages {
    stage("setup") {
      steps {
        sh "pip3 install --user -r Requirements.txt"
      }
    }
    stage("build") {
      parallel {
          stage("test") {
            steps {
              sh 'python3 -m unittest discover -s "tests"'
            }
          }
          stage("runApp") {
            steps {
              sh "python3 main.py"
            }
          }
       }
     }
  }
  post {
    always {
      sh 'curl -X POST "https://api.github.com/repos/msrpcoder/calc-app/statuses/$GIT_COMMIT?access_token=$GITHUB_TOKEN" -H "Content-Type: application/json" -H "Authorization: token $GITHUB_TOKEN"  -d \'{"state": "' + currentBuild.currentResult.toLowerCase() + '", "target_url": "' + env.BUILD_URL + '"}\''
    }
  }
}
