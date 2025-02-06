# Ansible-Installation

Below is a concise summary of the steps you took to successfully install Ansible and the required Juniper libraries (`junos-eznc` and `jxmlease`) on your Ubuntu 22.04 system:

1. **Install & Update Dependencies**  
   - Ran standard updates and installed the basic development tools to ensure you had the prerequisites for building Python modules:
     ```bash
     sudo apt update
     sudo apt install -y python3-pip python3-dev python3-venv libxml2-dev libxslt1-dev libssl-dev libffi-dev build-essential
     ```
   - Upgraded `pip`, `setuptools`, and `wheel` (even though some version conflicts remained):
     ```bash
     pip3 install --upgrade pip setuptools wheel
     ```

2. **Install/Verify Ansible**  
   - Installed Ansible from Ubuntu repositories (or it was already present):
     ```bash
     sudo apt update
     sudo apt install ansible -y
     ```
   - Confirmed installation via:
     ```bash
     ansible --version
     root@ubuntu-22-04:~# ansible --version
      ansible 2.10.8
      config file = None
      configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
      ansible python module location = /usr/lib/python3/dist-packages/ansible
      executable location = /usr/bin/ansible
      python version = 3.10.12 (main, Jan 17 2025, 14:35:34) [GCC 11.4.0]
     ```

3. **Address `setuptools` Version Conflict**  
   - Encountered errors with the `ncclient` package that required a specific `setuptools` version.  
   - Downgraded `setuptools` to avoid the `canonicalize_version()` conflict:
     ```bash
     pip3 install --upgrade "setuptools<66"
     ```

4. **Manually Install `ncclient`**  
   - Instead of installing the older pinned `ncclient==0.6.15`, you installed the latest `ncclient` directly from GitHub to bypass the setup error:
     ```bash
     pip3 install git+https://github.com/ncclient/ncclient.git@master
     ```

5. **Install `junos-eznc` and `jxmlease`**  
   - With the above adjustments in place, you were finally able to install:
     ```bash
     pip3 install junos-eznc jxmlease
     ```

6. **Verification**  
   - Confirmed that both libraries installed successfully by importing them in a Python one-liner:
     ```bash
     python3 -c "import jnpr.junos; print('junos-eznc installed successfully')"
     python3 -c "import jxmlease; print('jxmlease installed successfully')"
     root@ubuntu-22-04:~# python3 -c "import jnpr.junos; print('junos-eznc installed successfully')"
      junos-eznc installed successfully
      root@ubuntu-22-04:~# python3 -c "import jxmlease; print('jxmlease installed successfully')"
      jxmlease installed successfully
     ```

These steps resolved the conflicts between Python packages and allowed you to install Ansible along with the Juniper Python libraries needed for interacting with Junos and JunosEvo.
