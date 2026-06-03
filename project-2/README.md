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

[Write any errors you hit and how you fixed them]

---

### Live Project

Server IP: [102.37.130.227]

---

_Part of DecodeLabs Industrial Training Kit — Batch 2026_
```
