#!/usr/bin/env python3
import os
import subprocess
import sys
import urllib.request
import zipfile

JDK_PATH = os.path.expanduser("C:\\Java")

JDK_URLS = {
    "17": "https://download.java.net/java/GA/jdk17/latest/binaries/openjdk-17_windows-x64_bin.zip",
    "21": "https://download.java.net/java/GA/jdk21/latest/binaries/openjdk-21_windows-x64_bin.zip"
}

def download_and_extract(version, url):
    os.makedirs(JDK_PATH, exist_ok=True)
    zip_path = os.path.join(JDK_PATH, f"jdk{version}.zip")
    print(f"Downloading JDK {version}...")
    urllib.request.urlretrieve(url, zip_path)
    print(f"Extracting JDK {version}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(JDK_PATH, f"jdk-{version}"))
    os.remove(zip_path)

def set_env(var, value):
    subprocess.run(f'setx {var} "{value}"', shell=True)
    print(f"Set {var}={value}")

def main():
    for ver, url in JDK_URLS.items():
        download_and_extract(ver, url)

    print("Setting JAVA_HOME to JDK 21 by default...")
    set_env("JAVA_HOME", os.path.join(JDK_PATH, "jdk-21"))
    set_env("PATH", f"{os.path.join(JDK_PATH, 'jdk-21','bin')};%PATH%")
    
    print("✅ Windows setup complete! To switch JDK versions, update JAVA_HOME to the desired version and restart your terminal.")

if __name__ == "__main__":
    main()
