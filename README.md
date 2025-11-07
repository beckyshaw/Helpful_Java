# Java Multi-Version Setup Scripts

This repository provides scripts to **install and manage multiple Java versions** (JDK 17, JDK 21, etc.) on **Debian, Ubuntu, and Windows**. The scripts allow you to switch between versions easily, ensuring a flexible development environment.

## Features

- Install JDK 17 and JDK 21 automatically.
- Configure the system to switch between Java versions freely.
- Works on **Debian**, **Ubuntu**, and **Windows**.
- Cross-platform compatibility with separate scripts for each OS.

## Directory Structure
- **Installers/**
  - `debian_setup.py`
  - `ubuntu_setup.py` 
  - `windows_setup.py`
- License
- README.md


## Usage

### Debian
```
sudo python3 debian_setup.py
```

### Ubuntu
```
sudo python3 ubuntu_setup.py
```

### Windows
```
python3 windows_setup.py
```


### Switching
sudo update-alternatives --config java
sudo update-alternatives --config javac



## Contributing

Contributions are welcome! Please open a pull request or raise an issue for improvements or bugs.

⚠️ Only contributors with permissions to modify the repository can merge changes.
