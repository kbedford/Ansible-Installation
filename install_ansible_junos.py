#!/usr/bin/env python3
import os
import sys
import subprocess

def run_cmd(cmd, description=None):
    """
    Runs a shell command. Exits on error to stop the script.
    """
    if description:
        print(f"\n[STEP] {description}")
    print(f"Executing: {cmd}")
    
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"ERROR: Command failed with exit code {result.returncode}. Exiting.")
        sys.exit(result.returncode)

def main():
    # 1. Check if running as root
    if os.geteuid() != 0:
        print("Please run this script as root or use sudo. Exiting.")
        sys.exit(1)

    # 2. System Update & Install Dependencies
    run_cmd("apt update -y", description="Updating package lists")
    run_cmd("apt upgrade -y", description="Upgrading installed packages")
    run_cmd(
        "apt install -y python3-pip python3-dev python3-venv "
        "libxml2-dev libxslt1-dev libssl-dev libffi-dev build-essential ansible",
        description="Installing system prerequisites & Ansible"
    )

    # 3. Upgrade or Downgrade python packages to avoid conflicts
    #    (Setuptools<66 helps avoid the `canonicalize_version()` conflict with ncclient.)
    run_cmd('pip3 install --upgrade "setuptools<66" wheel', 
            description="Ensuring setuptools version is compatible")

    # 4. Install ncclient directly from GitHub
    #    (This bypasses older pinned versions with metadata issues.)
    run_cmd("pip3 install git+https://github.com/ncclient/ncclient.git@master",
            description="Installing ncclient from GitHub")

    # 5. Install junos-eznc & jxmlease
    run_cmd("pip3 install junos-eznc jxmlease", description="Installing junos-eznc and jxmlease")

    # 6. Verify Installations
    #    If any import fails, we'll see an error and exit.
    print("\n[STEP] Verifying junos-eznc...")
    subprocess.run('python3 -c "import jnpr.junos; print(\'junos-eznc installed successfully\')"', shell=True, check=True)

    print("[STEP] Verifying jxmlease...")
    subprocess.run('python3 -c "import jxmlease; print(\'jxmlease installed successfully\')"', shell=True, check=True)

    print("\n[INFO] Installation completed successfully!")
    print("[INFO] You can now use Ansible to manage Junos devices.")

if __name__ == "__main__":
    main()

