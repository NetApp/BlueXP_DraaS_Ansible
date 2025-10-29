import ansible_runner
import os
import time

# Automating the process -> create src/dest sites, add src/dest vcenters, create Replication Plan, create Resource Groupe.

script_dir = os.path.dirname(os.path.abspath(__file__))
private_data_dir = os.path.join(os.getcwd(), 'vars')
vars_file_path = os.path.join(script_dir, 'vars/env/extravars.yaml')
os.makedirs(private_data_dir, exist_ok=True)

def create_src_site():
    create_src_site_script_path = os.path.join(script_dir, 'create-src-site.yaml')
    draas_ansible_runner(create_src_site_script_path)

def create_dest_site():
    create_dest_site_script_path = os.path.join(script_dir, 'create-dest-site.yaml')
    draas_ansible_runner(create_dest_site_script_path)

def add_src_vcenter():
    add_src_vcenter_path = os.path.join(script_dir, 'add-src-vcenter.yaml')
    draas_ansible_runner(add_src_vcenter_path)

def add_dest_vcenter():
    add_dest_vcenter_path = os.path.join(script_dir, 'add-dest-vcenter.yaml')
    draas_ansible_runner(add_dest_vcenter_path)

def create_resourcegroup():
    create_resourcegroup_script_path = os.path.join(script_dir, 'create-resourcegroupe.yaml')
    draas_ansible_runner(create_resourcegroup_script_path)

def create_replicationplan():
    create_replicationplan_script_path = os.path.join(script_dir, 'create-replicationplan.yaml')
    draas_ansible_runner(create_replicationplan_script_path)

def run_compliance_check():
    run_compliance_check_script_path = os.path.join(script_dir, 'run_compliance_check.yaml')
    draas_ansible_runner(run_compliance_check_script_path)

def run_failback():
    run_failback_script_path = os.path.join(script_dir, 'run_failback.yaml')
    draas_ansible_runner(run_failback_script_path)

def run_failover():
    run_failover_script_path = os.path.join(script_dir, 'run_failover.yaml')
    draas_ansible_runner(run_failover_script_path)

def draas_ansible_runner(ansible_script_path):
    try:
        r = ansible_runner.run(
            private_data_dir=private_data_dir,
            playbook=ansible_script_path,
            extravars=vars_file_path
        )
        print(r.status)
    except Exception as e:
        print("Error running ansible script. PATH: ",  ansible_script_path)
    return True

if __name__ == "__main__":
    create_src_site()
    create_dest_site()
    add_src_vcenter()
    add_dest_vcenter()

    print("Waiting for 10 seconds until the sites and the vcenter are ready...")
    time.sleep(10) 

    create_resourcegroup()
    create_replicationplan()
    time.sleep(10) 
    
    print("Waiting for 10 seconds until the replication plan is ready...")
    run_compliance_check()
    run_failback()
    run_failover()

    
    

    