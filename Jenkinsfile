def tag = URLDecoder.decode(env.BUILD_TAG).replace('/', '-')

pipeline {
  environment {
    GITHUB_TOKEN = credentials('github-token')
    DOCKER_HUB_CREDENTIALS = credentials('dockerhub')
  } <<
  << << < task / docker
  agent any
  stages {
    stage("updateStatusToPending") {
      steps {
        sh 'curl -X POST https://api.github.com/repos/msrpcoder/calc-app/statuses/$GIT_COMMIT?access_token=$GITHUB_TOKEN -H "Content-Type: application/json" -H "Authorization: token $GITHUB_TOKEN" -d \'{"state": "pending", "context": "Jenkins Build", "description": "Project is running.", "target_url": "' + env.BUILD_URL + '"}\''
      }
    }
    stage("setupAndBuild") {
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
                stage("lint") {
                  steps {
                    sh "pylint main.py tests"
                  }
                }
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
                      archiveArtifacts artifacts: "test-run-result.xml", allowEmptyArchive: true
                      junit testResults: "test-run-result.xml", allowEmptyResults: true

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
    }
    stage("buildImage") {
      agent {
        label "first-vm"
      }
      stages {
        stage("build") {
          steps {
            sh "docker build -t mangudocker/calc-app:latest -t mangudocker/calc-app:${tag} ."
          }
        }
        stage("push") {
          steps {
            sh 'docker login -u $DOCKER_HUB_CREDENTIALS_USR -p $DOCKER_HUB_CREDENTIALS_PSW'
            sh "docker push mangudocker/calc-app:${tag}"
            sh "docker push mangudocker/calc-app:latest"
          }
          post {
            always {
              sh "docker image rm mangudocker/calc-app:${tag}"
              sh "docker image rm mangudocker/calc-app:latest"
              sh "docker logout"
            }
          }
        }
      }
    }
  }
  post {
    always {
      script {
        def status = currentBuild.currentResult.toLowerCase()
        status = status == 'aborted' ? 'failure' : status
        sh 'curl -X POST "https://api.github.com/repos/msrpcoder/calc-app/statuses/$GIT_COMMIT?access_token=$GITHUB_TOKEN" -H "Content-Type: application/json" -H "Authorization: token $GITHUB_TOKEN"  -d \'{"state": "' + status + '", "target_url": "' + env.BUILD_URL + '"}\''
      }
    }
  }
}
