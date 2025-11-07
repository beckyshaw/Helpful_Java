#!/usr/bin/env python3
import os
import subprocess
import sys
    

def run(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Command failed: {cmd}")
        sys.exit(1)

def download_jdks():
    print("Downloading OpenJDK 17 and 21")
    run("sudo apt install openjdk-17-jdk openjdk-21-jdk")

def install_jdks():
    print("Updating package list...")
    run("sudo apt update")
    print("Installing OpenJDK 17 and 21...")
    run("sudo apt install -y openjdk-17-jdk openjdk-21-jdk")

def setup_alternatives():
    print("Setting up update-alternatives...")
    jdks = {
        "17": "/usr/lib/jvm/java-17-openjdk-amd64",
        "21": "/usr/lib/jvm/java-21-openjdk-amd64"
    }
    for ver, path in jdks.items():
        run(f"sudo update-alternatives --install /usr/bin/java java {path}/bin/java {int(ver)*10+1}")
        run(f"sudo update-alternatives --install /usr/bin/javac javac {path}/bin/javac {int(ver)*10+1}")
    print("Setting JDK 21 as default...")
    run("sudo update-alternatives --set java /usr/lib/jvm/java-21-openjdk-amd64/bin/java")
    run("sudo update-alternatives --set javac /usr/lib/jvm/java-21-openjdk-amd64/bin/javac")

def create_aliases():
    bashrc = os.path.expanduser("~/.bashrc")
    aliases = """
# JDK switch aliases
alias jdk17='export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 && export PATH=$JAVA_HOME/bin:$PATH'
alias jdk21='export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64 && export PATH=$JAVA_HOME/bin:$PATH'
"""
    with open(bashrc, "a") as f:
        f.write(aliases)
    print("Aliases added to ~/.bashrc. Run `source ~/.bashrc` to activate them.")

def main():
    install_jdks()
    setup_alternatives()
    create_aliases()
    print("✅ Ubuntu setup complete! Use `sudo update-alternatives --config java` or aliases to switch.")

if __name__ == "__main__":
    main()
