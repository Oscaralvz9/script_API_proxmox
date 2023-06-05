from proxmoxer import ProxmoxAPI
import random
import string

proxmox = ProxmoxAPI("vidal99.softether.net", user="api@pve", password="password", verify_ssl=False)

def generate_container_id():
    return random.randint(100, 999)  

def generate_container_name():
    prefix = "container_"
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))  
    return prefix + suffix

vm_node = "node1" 
vm_os = "local:vztmpl/debian-11-turnkey-lamp_17.1-1_amd64.tar.gz" 


def create_container():
    vm_id = generate_container_id()
    vm_name = generate_container_name()

    proxmox.nodes(vm_node).lxc.create(
        vmid=vm_id,
        ostemplate=vm_os,
        storage="local-lvm",
        memory=512,
        cores=1,
        start=1
    )

    print(f"Contenedor '{vm_name}' con ID '{vm_id}' creado exitosamente en el nodo '{vm_node}'.")

create_container()
