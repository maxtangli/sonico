# chef

components
- chef dsl
- recipe, cookbook, chef-supermarket
- kitchen, chef-client, chef-server, chef-zero
- resources: package, service, cookbook-file, template

# tutorial

https://learn.chef.io/modules/learn-the-basics/ubuntu/virtualbox/set-up-a-machine-to-manage#/
~~~~
# local-mode
curl https://omnitruck.chef.io/install.sh | sudo bash -s -- -P chefdk -c stable -v 2.5.3
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

sudo chef-client --local-mode --runlist 'recipe[motd]'
cat /etc/motd
~~~~
