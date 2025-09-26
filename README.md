# BlueXP DRaaS Ansible Playbooks

This repository contains Ansible playbooks for automating interactions with BlueXP Disaster Recovery as a Service (DRaaS). The provided playbooks allow you to manage access tokens, discover virtual machines, retrieve and edit replication plans, and get detailed information about virtual machines.

## License
By accessing, downloading, installing or using the content in this repository, you agree the terms of the License laid out in License file.

Note that there are certain restrictions around producing and/or sharing any derivative works with the content in this repository. Please make sure you read the terms of the License before using the content. If you do not agree to all of the terms, do not access, download or use the content in this repository.

Copyright: 2025 NetApp Inc.

## Prerequisites
Before using these playbooks, ensure you have the following:
- Ansible installed on your machine.
- Valid credentials for BlueXP DRaaS.
- Refresh token and relevant IDs for your BlueXP account.

## Playbooks

### 1. `access_token.yaml`

**Purpose**: Obtains an access token from BlueXP using the provided refresh token. This token is used for authenticating subsequent API calls. 

### 2. `discovery.yaml`

**Purpose**: Discovers new virtual machines (VMs) to be added to the replication plan and refreshes existing VMs.

### 3. `get-replicationplan.yaml`

**Purpose**: Retrieves detailed information about all current replication plans. The gathered information is used for editing replication plans.

### 4. `edit-replication.yaml`

**Purpose**: Allows adjustments to the current replication plan in BlueXP DRaaS.

### 5. `get-vm.yaml`

**Purpose**: Retrieves detailed information about all available VMs in the source vcenter.

## Main Configuration

All required variables are defined in the `vars/env/extravars` file. Ensure this file is updated with your specific details before running the playbooks.

## Required Variables
- token: "" # Available at https://services.cloud.netapp.com/refresh-token
- clientid: "Mu0V1ywgYteI6w1MbD15fKfVIUrNXGWC" # No need to change this - Same for all api calls.
- agentid: "" # BlueXP Connector Agent ID
- authorization: "Bearer " #Put you access token after `Bearer`, this will be obtained by running "access_token.yaml" playbook.
- accountid: "" # BlueXP account ID
- replicationplanid: "" # Replication plan ID obtained through `get-replication` task.
- vcenterid: "" # Source VCenter ID - obtained Through `get-replication` task.

## Usage
Set Up Variables: Update the vars/env/extravars file with your specific values.

## Full Automation cycle to add Sites/vCenters, add Resource Groups and add a Replication Plan.
- Run `draas_runner.py` to get the access token:
  ```sh
  # This python script will automate the full cycle. You still can run the .yaml files separately (make sure to add the needed vars manually as this script automatically gather/restore the needed vars.)
  python3 draas_runner.py
  # After running this automation you can test the failover through the created ReplicationPlan, then you need to cleanup the test failover.
  ```

## Run Playbooks:
- Run `access_token.yaml` to get the access token:
  ```sh
  ansible-playbook access_token.yaml
  ```

- Run `discovery.yaml` to discover and refresh VMs:
  ```sh
  ansible-playbook discovery.yaml
  ```

- Run `add-src-site.yaml` to add a source to a site "info will be stored at vars/src_site.json".
  ```sh
  ansible-playbook add-src-site.yaml

- Run `add-dest-site.yaml` to add a dest to a site "info will be stored at vars/dest_site.json".
  ```sh
  ansible-playbook add-dest-site.yaml

- Run `add-src-vcenter.yaml` to add a source vcenter to a site. where you want run a failover for. "info will be stored at vars/src_vcenter.json" :
  ```sh
  ansible-playbook add-src-vcenter.yaml
  ```

- Run `add-dest-vcenter.yaml` to add a destination vcenter to a site. "info will be stored at vars/dest_vcenter.json":
  ```sh
  ansible-playbook add-dest-vcenter.yaml
  ```

- Run `create_resourcegroupe.yaml` to create a resource groupe "info will be stored at vars/src_site.json".
  ```sh
  ansible-playbook create_resourcegroupe.yaml

- Run `create_replicationplan.yaml` to create a replication plan (need the rg id) "info will be stored at vars/src_site.json".
  ```sh
  ansible-playbook create_resourcegroupe.yaml

- Run `get-replicationplan.yaml` to retrieve replication plans:
  ```sh
  ansible-playbook get-replicationplan.yaml
  ```

- Run `edit-replication.yaml` to edit the replication plan:
  ```sh
  ansible-playbook edit-replication.yaml
  ```

- Run `get-vms.yaml` to get all VMs details in a specified vCenter:
  ```sh
  ansible-playbook get-vms.yaml
  ```

- Run `get-vm-details.yaml` to get a specified VM information:
  ```sh
  ansible-playbook get-vm-details.yaml
  ```

- Run `get-sites` to get all sites and their vCenters:
  ```sh
  ansible-playbook sites.yaml
  ```

- Run `get-vcenters` to get all vCenters information:
  ```sh
  ansible-playbook sites.yaml
  ```

### Note
Ensure that all necessary credentials and IDs are correctly set in the `vars/env/extravars` file before running the playbooks and the Python runner.

## Author Information
- [Ayman Soliman](mailto:ayman.soliman@netapp.com) - NetApp Solutions Engineering Team
- [Pradeep Kumar](mailto:pradeep.kumar@netapp.com) - NetApp Solutions Engineering Team
- [Niyaz Mohamed](mailto:niyaz.mohamed@netapp.com) - NetApp Solutions Engineering Team