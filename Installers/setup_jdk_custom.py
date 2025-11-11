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

# --- JDK Installers ---

def install_jdk(version):
    print(f"\n=== Installing OpenJDK {version} ===")
    run("sudo apt update -y")
    run(f"sudo apt install -y openjdk-{version}-jdk")

# --- Setup alternatives ---

def setup_alternatives(selected_versions):
    print("\nSetting up update-alternatives...")
    for version in selected_versions:
        java_path = f"/usr/lib/jvm/java-{version}-openjdk-amd64/bin/java"
        javac_path = f"/usr/lib/jvm/java-{version}-openjdk-amd64/bin/javac"
        run(f"sudo update-alternatives --install /usr/bin/java java {java_path} {version}0")
        run(f"sudo update-alternatives --install /usr/bin/javac javac {javac_path} {version}0")

# --- Aliases ---

def create_aliases(selected_versions):
    zshrc = os.path.expanduser("~/.zshrc")
    print("\nAdding JDK switch aliases...")
    aliases = "\n# --- JDK switch aliases ---\n"
    for version in selected_versions:
        aliases += f"alias jdk{version}='export JAVA_HOME=/usr/lib/jvm/java-{version}-openjdk-amd64 && export PATH=$JAVA_HOME/bin:$PATH'\n"
    with open(zshrc, "a") as f:
        f.write(aliases)
    print("✅ Aliases added to ~/.zshrc. Run `source ~/.zshrc` to activate them.")

# --- Starting point ---
import time

def print_banner():
    print("""
=====================================
     ☕  Java Environment Installer
=====================================
""")
    print("Initializing installer...")
    time.sleep(0.5)
    print("Ready to install selected JDK versions!\n")

# --- User selection ---

AVAILABLE_JDKS = ["8", "11", "17", "21"]

def install_jdks():
    print("Available JDKs: " + ", ".join(f"JDK {v}" for v in AVAILABLE_JDKS))
    choice = input("\nEnter JDK versions to install (comma-separated, e.g., 17,21): ").replace(" ", "")
    selected = [v for v in choice.split(",") if v in AVAILABLE_JDKS]
    if not selected:
        print("No valid versions selected. Exiting.")
        sys.exit(1)

    for version in selected:
        install_jdk(version)
    
    setup_alternatives(selected)
    create_aliases(selected)

# --- Main ---

def main():
    print_banner()
    install_jdks()
    print("\n✅ Debian JDK setup complete! Use `jdk<version>` to switch versions or update-alternatives to choose manually.")

if __name__ == "__main__":
    main()
