#!/bin/sh

sudo apt update 

wget -O - "https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc" | sudo apt-key add -

sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list <<EOF

deb https://dl.bintray.com/rabbitmq-erlang/debian bionic erlang
deb https://dl.bintray.com/rabbitmq/debian bionic main

EOF


sudo apt-get update -y

sudo apt-get install rabbitmq-server -y

#Check RabbitMQ Server Status.
#sudo systemctl status rabbitmq-server.service

#If RabbitMQ is not running, then start service with this command:
#sudo systemctl start rabbitmq-server.service

#Enable RabbitMQ service on system boot.
sudo systemctl enable rabbitmq-server

#RabbitMQ management console runs on port 15672
# and it needs to be granted permission via the firewall.

sudo ufw allow 15672

#Let us see how we can enable the ‘Installation Management Console’ plugin. 
#But before we do that, let us take a look at all the RabbitMQ plugins that are available.

#sudo rabbitmq-plugins list

#Now enable the RabbitMQ Management plugin
sudo rabbitmq-plugins enable rabbitmq_management

#Here we create a user with username ‘admin’ and password is also ‘admin’. 
sudo rabbitmqctl add_user admin admin

#Now we tag our user ‘admin’, which we created in the steps above, as ‘administrator’
sudo  rabbitmqctl set_user_tags admin administrator

#Now we are ready to restart RabbitMQ service
sudo systemctl restart rabbitmq-server.service

