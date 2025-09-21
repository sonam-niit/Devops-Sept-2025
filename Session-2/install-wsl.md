# Install WSL Windows SubSystem for Linux

1. Open PowerShell as Administrator. / open CMD as Administrator
2. Run this command to enable WSL and install Ubuntu by default
```bash
wsl --install
```
3. set up username and password for default user
    - give your name
    - give password which can be easily remember
    - like admin
4. Restart your computer when prompted.

# How to open WSL

1. open cmd and type wsl and it will open
2. directly search for wsl and open that application

# Incase if you are facing any problem like 
- The server name or address could not be resolved
- then try to install it manually by doing below setup

1. run below commands in terminal
```bash
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
2. Restrat System
3. Install/update WSL
```bash
wsl --install --no-distribution
```
4. Update WSL
```bash
wsl update
```
5. install ubuntu
```bash
wsl --install -d ubuntu
```
6. Vefify
```bash
wsl --list --verbose
```