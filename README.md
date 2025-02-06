Below is an install_ansible_junos.py script you can run as root (or via sudo) to automatically:

1. Update your Ubuntu packages  
2. Install system prerequisites  
3. Install or update Ansible  
4. Downgrade `setuptools` (to avoid a known conflict with `ncclient`)  
5. Install `ncclient` from GitHub  
6. Install `junos-eznc` and `jxmlease`  
7. Verify the installations  

You can copy and paste the script into a file (e.g., `install_ansible_junos.py`) and then run it with `sudo python3 install_ansible_junos.py`.

### **How to Use**

1. **Save the Script**  
   Copy the script into a file called `install_ansible_junos.py`.

2. **Make It Executable (Optional)**  
   ```bash
   chmod +x install_ansible_junos.py
   ```

3. **Run the Script as Root**  
   ```bash
   sudo python3 install_ansible_junos.py
   ```
   or
   ```bash
   sudo ./install_ansible_junos.py
   ```

4. **Verify Ansible Version**  
   After successful completion, confirm Ansible is installed:
   ```bash
   ansible --version
   ```

5. **Use Ansible with Junos**  
   You can now create your `inventory` and `playbooks` to manage Junos/Evo devices.

---

### **What This Script Does**

1. **System Update & Package Installation**  
   - Updates apt repositories (`apt update`)  
   - Upgrades existing packages (`apt upgrade`)  
   - Installs Python build tools, libraries, and **Ansible**.

2. **Downgrades `setuptools`**  
   - Installs a version of `setuptools` (<66) to avoid the `canonicalize_version()` conflict when building `ncclient`.

3. **Installs `ncclient` from GitHub**  
   - Installs the latest `ncclient` code from GitHub to bypass metadata-generation issues with older pinned versions (`ncclient==0.6.15`).

4. **Installs `junos-eznc` and `jxmlease`**  
   - Installs the official Juniper Python library (`junos-eznc`) and `jxmlease` for working with Junos devices.

5. **Verifies the Installation**  
   - Imports both `jnpr.junos` and `jxmlease` in Python to confirm successful installation.
![image](https://github.com/user-attachments/assets/1c7660fe-defd-452a-9543-cc8c98d9b2c0)

---

You should now have **Ansible** and all **Juniper-related Python packages** installed and working on your Ubuntu 22.04 system. Enjoy automating your Junos devices!
