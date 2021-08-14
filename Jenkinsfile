pipeline {
  environment {
    GITHUB_TOKEN = credentials('github-token')
  }
  agent {
    docker {
      image "python:latest"
      args "--user root"
      label "first-vm"
    }
  }
  stages {
    stage("setup") {
      steps {
        sh "pip3 install virtualenv && virtualenv test && sh ./test/bin/activate && pip3 install -r Requirements.txt"
      }
    }
    stage("build") {
      stages {
          stage("test") {
            parallel {
              stage("unittest") {
                steps {
                  sh 'python3 -m unittest discover -s "tests"'
                }
              }
              stage("pytest") {
                steps {
                  sh 'PYTHONPATH=$(pwd):$PYTHONPATH py.test --junitxml=test-run-result.xml'
                }
                post {
                  always {
                    archiveArtifact artifacts:"test-run-result.xml", allowEmptyArchive: true
                  }
                }
              }
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
