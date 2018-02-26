# Jenkins

tutorial
- [x] setup via docker 0.5h
- [x] setup via native 0.5h

- [x] bug: failed to run pipeline <- git too old in centos7.4 1h
- [x] guided tour https://jenkins.io/doc/pipeline/tour/getting-started/ 1h
- [x] using jenkins

# summary

features
- continuous delivery pipeline: code to automated vcs -> user.
- Jenkins Pipeline: a suite of plugins to make a continuous delivery pipeline.
- pipeline: stages&steps, post, agent, environment variables, etc.
- blue ocean: user-friendly pipeline editor.

pros
- a platform which integrate tools to support CI/CD. 

cons
- unmaintained plugins.
- java app: not microservice.
- local file storage: io performace issue, backup issue.
- fragment files
- slow start

Jenkinsfile
~~~~
pipeline {
    agent { docker 'ruby' }
    stages {
        stage('build') {
            steps {
				sh 'echo "hello, jenkins!"'
                sh 'ruby --version'
            }
        }
		stage('Deploy') {
            steps {
                retry(3) {
                    sh 'echo "retry, jenkins!"'
                }

                timeout(time: 3, unit: 'MINUTES') {
                    sh 'echo "timeout, jenkins!"'
                }
            }
        }
		stage('Test') {
			steps {
				sh 'echo "Fail!"; exit 1'
			}
		}
    }
	post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
~~~~

# setup

setup 
~~~~
# via docker: https://github.com/jenkinsci/docker/blob/master/README.md
nohup docker run -p 8080:8080 -p 80:80 jenkins/jenkins:lts &
nohup docker run -p 8080:8080 -p 80:80 maxtangli/jenkins:init &
less nohup.out
/password

# or via native
sudo yum install java
wget http://mirrors.jenkins.io/war-stable/latest/jenkins.war
java -jar jenkins.war --httpPort=8080
~~~~

config
- config via web: localhost:8080
- force english ui: https://wiki.jenkins.io/display/JENKINS/Locale+Plugin
- install newest git in centos7.4
~~~~
wget https://setup.ius.io/ && mv index.html setup_ius.sh && chmod 755 setup_ius.sh && sudo ./setup_ius.sh
sudo yum install git2u
~~~~