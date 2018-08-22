import subprocess



subprocess.call('sudo mv my_assistant_one.service /lib/systemd/system/',shell = True)
subprocess.call('sudo systemctl enable my_assistant_one.service',shell = True)
subprocess.call('sudo service my_assistant_one start',shell=True)
