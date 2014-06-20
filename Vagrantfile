# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # For a complete reference, see the online documentation at vagrantup.com.

  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.provision :shell, :path => "bootstrap.sh"
  config.vm.network :forwarded_port, guest: 8000, host: 8000
  config.vm.network :forwarded_port, guest: 8080, host: 8080
  config.vm.network :forwarded_port, guest: 3306, host: 3306
  config.vm.provider :virtualbox do |vb|
    vb.name = "celery-feed-aggregator"
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end

end
