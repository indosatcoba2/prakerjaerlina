# -*- coding: utf-8 -*-
"""Salinan dari xrdp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XQ2ovv2ee0sr5QI53AgdDzrhyZ_kcJ4p
"""

#@title **Create User**
import os
username = "akuhnet" #@param {type:"string"}
password = "123456" #@param {type:"string"}

print("Creating User and Setting it up")

# Creat user
os.system(f"useradd -m {username}")

# Add user to sudo group
os.system(f"adduser {username} sudo")

# Set password user to 'root'
os.system(f"echo '{username}:{password}' | sudo chpasswd")

# Change default shell from sh to bash
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

print("User Created and Configured")

#@title **Google Drive Mount**

from google.colab import drive
drive.mount('/content/drive')

#@title **Start RDP**
#@markdown UPDATE<br>
#@markdown Connect with RDP<br><br>
#@markdown [Ngrok Auth Token](https://dashboard.ngrok.com/get-started/your-authtoken)<br><br>
#@markdown Other Free VPS
#@markdown [akuh.net](https://www.akuh.net/)
! wget -O xfce4.sh https://bit.ly/akuhnetxrdpcolab > /dev/null 2>&1
! chmod +x xfce4.sh
! ./xfce4.sh