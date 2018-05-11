# chef

components
- chef dsl

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

# learning chef
