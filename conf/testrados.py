
import rados

cluster = rados.Rados(conffile="ceph.conf")
cluster.connect()
print(list(cluster.list_pools()))

