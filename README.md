Here's a simple Dockerized "Hello World" web application in Python (Flask) that:

1) Listens on two paths: /hello (open) and /hi (requires login).

2) Uses Basic Authentication for the /hi endpoint.

3) Is fully Dockerized.

project structure :

```
hello-app/
├── app.py
├── requirements.txt
└── Dockerfile
```

cd hello-app

### Create virtual environment
python3 -m venv venv

### Activate it
### On Linux/macOS:
source venv/bin/activate

### On Windows:
venv\Scripts\activate

### Navigate to project directory

```
cd hello-app
```

### Build Docker image

```
docker build -t hello-world-app .
```

### Run Docker container

```
docker run -p 5000:5000 hello-world-app
```

Test It

Visit http://localhost:5000/hello → you get Hello, World!

Visit http://localhost:5000/hi → browser will prompt for login.

Username: admin

Password: secret

### How to push image to Docker Hub

```
docker login -u anantgsaraf
```

```
(venv) root@DESKTOP-CL9FNGA:hello-app# docker push anantgsaraf/kong-routing-application:1.0.0
The push refers to repository [docker.io/anantgsaraf/kong-routing-application]
80b8f5be00cb: Pushed
ca0fcdba402f: Pushed
6d4364e95243: Pushed
a634fb2f77a2: Pushed
fab19f6d5974: Mounted from library/python
08f694c3ad40: Mounted from library/python
f65ccd2650d0: Mounted from library/python
ea680fbff095: Mounted from library/python
1.0.0: digest: sha256:2e0323a78d191e33512b5dfc622bdae905dcbccf1511820e295b1e784d30cfed size: 1990
(venv) root@DESKTOP-CL9FNGA:hello-app# 
```

### Deploy EKS cluster from here: 

```
https://gitlab.com/devops5113843/terraform/-/tree/main/26-EKS-with-LoadBalancer-Controller?ref_type=heads

```

### Step-02: Create S3 Bucket
- Go to Services -> S3 -> Create Bucket
- **Bucket name:** terraform-on-aws-eks
- **Region:** US-East (N.Virginia)
- **Bucket settings for Block Public Access:** leave to defaults
- **Bucket Versioning:** Enable
- Rest all leave to **defaults**
- Click on **Create Bucket**
- **Create Folder**
  - **Folder Name:** dev
  - Click on **Create Folder**
- **Create Folder**
  - **Folder Name:** dev/eks-cluster
  - Click on **Create Folder**  
- **Create Folder**
  - **Folder Name:** dev/app1k8s
  - Click on **Create Folder**    

### Step-05: Add State Locking Feature using DynamoDB Table
- Understand about Terraform State Locking Advantages
### Step-05-01: EKS Cluster DynamoDB Table
- Create Dynamo DB Table for EKS Cluster
  - **Table Name:** dev-ekscluster
  - **Partition key (Primary Key):** LockID (Type as String)
  - **Table settings:** Use default settings (checked)
  - Click on **Create**
### Step-05-02: App1 Kubernetes DynamoDB Table
- Create Dynamo DB Table for app1k8s
  - **Table Name:** dev-app1k8s
  - **Partition key (Primary Key):** LockID (Type as String)
  - **Table settings:** Use default settings (checked)
  - Click on **Create**

This is how we can deploy eks kong routing stack

here : https://github.com/Anantgs/EKS-BASE-STACK.git



