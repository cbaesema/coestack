#!/usr/bin/python


import os


#system update
print "running apt-get update"
os.system('apt-get update')
print "installing pre installation packages"
os.system('apt-get install -qym git puppet ipmitool python-software-properties')
print "cloning puppet manifests from CiscoSystems github repo"
os.system('rm -rf /opt/manifests')
os.system('git clone http://github.com/CiscoSystems/folsom-manifests.git -b multi-node /opt/manifests')
print "removing old manifests"
os.system('rm -rf /etc/puppet/manifests/*')
print "copy manifests to /etc/puppet/manifests"
os.system('cp /opt/manifests/manifests/* /etc/puppet/manifests')

