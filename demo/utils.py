import paramiko
import tempfile
import os
import re
from subprocess import call

CEPH_ADMIN = 'admin-node'
CEPH_ADMIN_PORT = 22
USERNAME = 'kostis'
PASSWORD = 'secretpw'
KEY_PATH = '/home/kostis/.ssh/id_rsa'
REMOTE_VAR_PATH = '/var/local/ceph-app'

def test_function():
    return get_data('test-object-3')
    #store_object('new-object', 'this is the data')

def _execute_cmd(cmd, username=USERNAME):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(CEPH_ADMIN, username=username)
    _, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.readlines()
    err = stderr.readlines()
    ssh.close()
    return out, err

def get_object_list():
    out, err = _execute_cmd('rados -p data ls')
    return [l.strip() for l in out]

def get_data(obj):
    out, err = _execute_cmd('/home/kostis/get_data.sh ' + str(obj))
    return ''.join(out).strip()

def delete_object(obj):
    _execute_cmd('rados rm %s -p data' % str(obj))

def store_object(name, data, username=USERNAME):
    with tempfile.NamedTemporaryFile() as f:
        f.write(str.encode(str(data)))
        f.flush()

        # Transfer the data file to the admin node
        transport = paramiko.Transport((CEPH_ADMIN, CEPH_ADMIN_PORT))
        key = paramiko.RSAKey.from_private_key_file(KEY_PATH)
        transport.connect(username=username, pkey=key)
        transport.open_channel("session", username, "localhost")
        sftp = paramiko.SFTPClient.from_transport(transport)
        remote_path = os.path.join(REMOTE_VAR_PATH, 
                                   os.path.basename(f.name))
        sftp.put(f.name, remote_path)
        transport.close()
        sftp.close()

        # insert the data into ceph
        _execute_cmd('rados put %s %s -p data' % (str(name), remote_path))

def is_valid_name(name):
    return bool(re.match(r'^[a-zA-Z0-9\-]+$', name))

def exists(name):
    return name in get_object_list()

def startup_cluster():
    call(['start-ceph'])

