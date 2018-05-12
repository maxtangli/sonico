# chef

https://docs.chef.io/chef_overview.html

develop
- workstation: chef dsl, recipe, cookbook
- chef-repo
- chef-development-kit: chef, knife
- test-kitchen: .kitchen.yml, chef-spec
- chef-supermarket

deploy
- chef server: cookbooks, policy settings, data bag, manage console. 
- policy: role, environment, secure data in data bag, cookbook version, run-list.
- node: server, cloud, vm, network device, container etc.
- chef on nodes: chef client, ohai

use market cookbook
~~~~
vim berksfile: cookbook xxx
berks vendor
vim recipes/default.rb: chef dsl by xxx
~~~~

run recipes locally
~~~~
chef generate cookbook cookbooks/tang-dev
vim ...
sudo chef-client -z -r 'recipe[tang-dev]'
~~~~

test with docker
~~~~
# docker installed
chef gem install kitchen-docker
kitchen converge 
~~~~

# install

chef-dk in ubuntu
~~~~
wget https://packages.chef.io/files/stable/chefdk/2.5.3/ubuntu/16.04/chefdk_2.5.3-1_amd64.deb
sudo dpkg -i chefdk_2.5.3-1_amd64.deb

chef generate app chef-repo
mkdir -p chef-repo/.chef && echo '.chef' >> chef-repo/.gitignore

# ignore: For a ChefDK installation that will interact with the Chef server
~~~~

# tutorial

https://learn.chef.io/modules/learn-the-basics/ubuntu/virtualbox/set-up-a-machine-to-manage#/
~~~~
# install
curl https://omnitruck.chef.io/install.sh | sudo bash -s -- -P chefdk -c stable -v 2.5.3

# local-mode
mkdir chef-repo && cd chef-repo
vim webserver.rb
sudo chef-client --local-mode webserver.rb 
curl localhost

# cookbook
mkdir cookbooks && sudo apt-get install tree
chef generate cookbook cookbooks/learn_chef_apache2 && tree cookbooks
chef generate template cookbooks/learn_chef_apache2 index.html && tree cookbooks
vim default.rb
sudo chef-client --local-mode --runlist 'recipe[learn_chef_apache2]'
curl localhost
~~~~

https://learn.chef.io/modules/create-a-web-app-cookbook/ubuntu/virtualbox/
~~~~
chef generate cookbook cookbooks/lamp
vim default.rb
~~~~

# Learning Chef.Mischa Taylor etc.2014.pdf

recipe
~~~~
sudo chef-apply webserver.rb
~~~~

cookbook
~~~~
chef generate cookbook motd && cd motd
kitchen list
sudo touch /etc/motd
chef generate file motd
vim files/default/motd
kitchen converge

sudo chef-client --local-mode --runlist 'recipe[motd]'
cat /etc/motd
~~~~
