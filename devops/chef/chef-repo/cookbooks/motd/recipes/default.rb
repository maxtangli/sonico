cookbook_file "/etc/motd" do
  source "motd"
  mode "0644"
end
