# vagrant

references
- https://www.vagrantup.com/intro/getting-started/index.html

~~~~
# stores the box under a specific name so that multiple Vagrant environments can re-use it
vagrant box add hashicorp/precise64

vagrant init
# edit Vagrantfile ...
vagrant up
vagrant reload

vagrant ssh
# synced folders: By default, Vagrant shares your project directory to the /vagrant directory

# edit config.vm.provision ...
# Alternatively, provisioning with Puppet, Chef, or Ansible
# For complex provisioning scripts, it may be more efficient to package a custom Vagrant box with those packages pre-installed

# edit config.vm.network ...

# public url to sharing env for development or Q/A 
vagrant share

# suspend: keep context and disk. halt: keep disk. destory: keep nothing.
vagrant suspend
vagrant halt
vagrant destory 

# multi-machine

# using Docker as a provider

# push: As of version 1.7, Vagrant is capable of deploying or "pushing" application code in the same directory as your Vagrantfile to a remote such as an FTP server.
~~~~