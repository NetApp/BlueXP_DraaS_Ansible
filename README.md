# BlueXP DRaaS Ansible Playbooks

This repository contains Ansible playbooks for automating interactions with BlueXP Disaster Recovery as a Service (DRaaS). The provided playbooks allow you to manage access tokens, discover virtual machines, retrieve and edit replication plans, and get detailed information about virtual machines.

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

All required variables are defined in the `vars/main.yaml` file. Ensure this file is updated with your specific details before running the playbooks.


## Required Variables
- token: "" # Available at https://services.cloud.netapp.com/refresh-token
- clientid: "Mu0V1ywgYteI6w1MbD15fKfVIUrNXGWC" # No need to change this - Same for all api calls.
- agentid: "" # BlueXP Connector Account ID
- authorization: "Bearer " #Put you access token after `Bearer`, this will be obtained by running "access_token.yaml" playbook.
- accountid: "" # BlueXP account ID
- replicationplanid: "" # Replication plan ID obtained through `get-replication` task.
- vcenterid: "" # Source VCenter ID - obtained Through `get-replication` task.

## Usage
Set Up Variables: Update the vars/main.yaml file with your specific values.

## Run Playbooks:

- Run `access_token.yaml` to get the access token:
  ```sh
  ansible-playbook access_token.yaml
  ```

- Run `discovery.yaml` to discover and refresh VMs:
  ```sh
  ansible-playbook discovery.yaml
  ```

- Run `get-replicationplan.yaml` to retrieve replication plans:
  ```sh
  ansible-playbook get-replicationplan.yaml
  ```

- Run `edit-replication.yaml` to edit the replication plan:
  ```sh
  ansible-playbook edit-replication.yaml
  ```

- Run `get-vm.yaml` to get VM details:
  ```sh
  ansible-playbook get-vm.yaml
  ```

### Note

Ensure that all necessary credentials and IDs are correctly set in the `vars/main.yaml` file before running the playbooks.

