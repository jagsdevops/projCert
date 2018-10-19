pipeline {
  agent any
  stages {
    stage('') {
      steps {
        ansiblePlaybook(playbook: ' /vagrant/jags-ansible-books/puppet-agent.yml', colorized: true, inventory: '/vagrant/inventory.ini')
      }
    }
  }
}