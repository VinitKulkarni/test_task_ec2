### Create a Ec2_instance:
``` sh
Type: t2.medium
Size: 30GB volume
```

### Ports allowed in Security Group:
``` sh
3000  -> frontend
5000  -> backend
8080  -> jenkins
27017 -> mongodb
22    -> ssh
```

### How to run the frontend:
``` sh
git clone https://github.com/VinitKulkarni/test_task_ec2.git
cd test_task_ec2/frontend
sudo apt install npm
npm install experss body-parser axios
node app.js
Now frontend can be accessed on internet: http://publicIP:3000
```

### How to run the backend:
``` sh
cd test_task_ec2/backend
create .env file and paste the MONGODB_URI
sudo apt update
sudo apt install python3-venv python3-pip
pip3 --version
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
Now backend is connected with frontend to store data in mongodb
```

### Install pm2 to run frontend and backend in background:
``` sh
sudo npm install pm2 -g  (Must install pm2 on globally)
Goto frontend directory. where app.js file is present. Now start frontend:
pm2 start app.js --name express-frontend

Goto backend directory. where app.py file is present. Now start backend:
pm2 start app.py --name flask-backend
``` 
### Install Jenkins:
``` sh
sudo apt update
sudo apt install openjdk-17-jre
java -version
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

### To access the jenkins:
``` sh
http://publicIP:8080

To get the inital password:
sudo cat /var/lib/jenkins/secrets/initialAdminPassword 

Install plugins and finish the setup
```
