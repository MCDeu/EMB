import configparser
import os

config = configparser.ConfigParser()
configFilePath = r'app.conf'
config.read(configFilePath)

lg_IP = config['INSTALLATION']['lg_IP']
lg_pass = config['INSTALLATION']['lg_pass']
project_location = config['INSTALLATION']['project_location']

folder_target = '/var/www/html/EMB'

#command = "sshpass -p {} ssh {} mkdir {}".format(lg_pass, lg_IP, folder_target)
#print(command)
#os.system(command)

command = "sshpass -p {} ssh {} \"echo -e ' \n' > /var/www/html/kmls.txt\"".format(lg_pass, lg_IP)
os.system(command)

command = "sshpass -p {} scp $HOME/{}EMB/Django/data/static/Logos.png {}:/var/www/html/EMB/Logos.png".format(lg_pass, project_location, lg_IP)
print(command)
os.system(command)
