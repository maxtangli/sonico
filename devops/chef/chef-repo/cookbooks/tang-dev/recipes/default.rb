# timezone
execute 'set-timezone' do
  command 'timedatectl set-timezone Asia/Tokyo'
end

# git
bash 'config-git' do
  code <<-EOH
    git config --global user.name tang
    git config --global user.email maxtangli@qq.com
    git config --global core.autocrlf input
  EOH
end

# rbenv
ruby_version = '2.5.1'
shell_user = 'vagrant'
rbenv_user_install shell_user
rbenv_ruby ruby_version do
  user shell_user
  verbose true
end
rbenv_global ruby_version do
  user shell_user
end

# ruby
gem_package 'bundler'
