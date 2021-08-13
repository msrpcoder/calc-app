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
    stage("runApp") {
      steps {
        sh "python3 main.py"
      }
    }
  }
  post {
    always {
      sh 'curl -X POST "https://api.github.com/repos/msrpcoder/calc-app/statuses/${GIT_COMMIT}?access_token=${GITHUB_TOKEN}" -H "Content-Type: application/json" -d "{\'status\': \'${currentBuild.currentResult}\', \'target_url\': \'${BUILD_URL}\'}"'
    }
  }
}
