## Project 2 — Virtual Server Deployment on Azure

### Objective

Act as a SysAdmin and provision a virtual server in the cloud, install a web server, and host a live webpage.

---

### Tools Used

- Microsoft Azure (Virtual Machine)
- Ubuntu Server 24.04 LTS
- Nginx Web Server
- SSH (Secure Shell)
- Terminal / Command Line

---

### What I Did

#### Step 1 — Created Azure Virtual Machine

- Created a Resource Group called `decodelabs-project2`
- Launched an Ubuntu VM (Standard B2ats v2 (2 vcpus, 1 GiB memory))
- Configured Network Security Group rules:
  - Port 22 (SSH)
  - Port 80 (HTTP)
  - Port 443 (HTTPS)
- Downloaded SSH key pair (.pem file)

#### Step 2 — Connected via SSH

```bash
chmod 400 /mnt/c/Users/Oluchi/Downloads/myVirtualMachine_key.pem
ssh -i ~/myVirtualMachine_key.pem azureuser@102.37.130.227
```

#### Step 3 — Installed Nginx

```bash
sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
```

#### Step 4 — Hosted Custom Webpage

- Navigated to `/var/www/html/`
- Edited `index.html` using nano
- Deployed custom "Welcome to DecodeLabs" page

```markdown
### Screenshots

**Azure VM Running:**

![Azure VM](project-2/Azure VM Running.png)

**SSH Connection:**

![SSH](project-2/SSH Terminal connection.png)

**Live Webpage:**

![Live Page](project-2/live webpage .png)
```

---

### What I Learned

- How cloud Virtual Machines work
- SSH key-based authentication
- Linux command line basics
- Web server configuration with Nginx
- Azure Portal navigation
- Network Security Groups (Firewall rules)
- The difference between Apache and Nginx
- Pets vs Cattle cloud philosophy

---

### Challenges I Faced

## 1. SSH Private Key Not Found

### Challenge

While attempting to connect to the Azure Virtual Machine using SSH, the system could not locate the private key file.

### Error

```bash
chmod: cannot access '/path/to/myVirtualMachine_key.pem': No such file or directory
```

### Solution

I realized that the command used a placeholder path. I located the actual private key file and specified the correct file path before retrying the command.

---

## 2. SSH Private Key Permission Error

### Challenge

After locating the private key file, SSH refused to use it because the file permissions were too open.

### Error

```bash
WARNING: UNPROTECTED PRIVATE KEY FILE!
Permissions 0555 are too open.
```

### Solution

The key file was stored on the Windows filesystem, which does not enforce Linux permissions correctly. I copied the key into my Linux home directory and restricted access using:

```bash
chmod 400 ~/myVirtualMachine_key.pem
```

This allowed SSH to use the private key securely.

---

## 3. Difficulty Accessing Files Between Windows and Linux (WSL)

### Challenge

The SSH key was initially stored in the Windows Downloads folder, making it difficult to manage permissions from the Linux environment.

### Solution

I accessed the Windows filesystem through WSL using the `/mnt/c` mount point and copied the file into my Linux home directory, where Linux permissions could be applied correctly.

---

## 4. Establishing Secure Remote Access to the Virtual Machine

### Challenge

Connecting to the Azure Virtual Machine required proper SSH authentication and key management.

### Solution

After correcting the key location and permissions, I successfully connected to the VM using:

```bash
ssh -i ~/myVirtualMachine_key.pem azureuser@<public-ip-address>
```

This provided secure remote administrative access to the server.

### Live Project

Server IP: [http://102.37.130.227/]

---
