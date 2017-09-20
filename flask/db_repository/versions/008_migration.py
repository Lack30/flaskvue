from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
api = Table('api', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('function', VARCHAR(length=64)),
    Column('ip', VARCHAR(length=20)),
    Column('username', VARCHAR(length=64)),
    Column('password', VARCHAR(length=64)),
)

hardware = Table('hardware', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('node_ip', VARCHAR(length=20)),
    Column('idrac_ip', VARCHAR(length=29)),
    Column('cpu', VARCHAR(length=64)),
    Column('memory', VARCHAR(length=64)),
    Column('disk', VARCHAR(length=64)),
    Column('power', VARCHAR(length=64)),
    Column('temp', VARCHAR(length=64)),
)

idrac = Table('idrac', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('idrac_ip', VARCHAR(length=20)),
    Column('username', VARCHAR(length=64)),
    Column('password', VARCHAR(length=64)),
    Column('node_ip', VARCHAR(length=20)),
)

node = Table('node', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('ip', VARCHAR(length=20)),
    Column('system', VARCHAR(length=30)),
    Column('hostname', VARCHAR(length=30)),
    Column('username', VARCHAR(length=64)),
    Column('password', VARCHAR(length=300)),
    Column('status', VARCHAR(length=64)),
)

sio_volume = Table('sio_volume', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('read', INTEGER(display_width=11)),
    Column('write', INTEGER(display_width=11)),
    Column('time', DATETIME),
)

user = Table('user', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('username', VARCHAR(length=15)),
    Column('password', VARCHAR(length=20)),
    Column('role', SMALLINT(display_width=6)),
)

vm_host = Table('vm_host', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('hostname', VARCHAR(length=64)),
    Column('cpuUsage', INTEGER(display_width=11)),
    Column('cpuTotal', INTEGER(display_width=11)),
    Column('memUsage', INTEGER(display_width=11)),
    Column('memTotal', INTEGER(display_width=11)),
    Column('uptime', INTEGER(display_width=11)),
)

vm_storage = Table('vm_storage', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('hostname', VARCHAR(length=64)),
    Column('free', INTEGER(display_width=11)),
    Column('total', INTEGER(display_width=11)),
)

vmware = Table('vmware', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('hostname', VARCHAR(length=64)),
    Column('power', VARCHAR(length=15)),
    Column('cpuUsage', INTEGER(display_width=11)),
    Column('ip', VARCHAR(length=15)),
    Column('uptime', INTEGER(display_width=11)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['api'].drop()
    pre_meta.tables['hardware'].drop()
    pre_meta.tables['idrac'].drop()
    pre_meta.tables['node'].drop()
    pre_meta.tables['sio_volume'].drop()
    pre_meta.tables['user'].drop()
    pre_meta.tables['vm_host'].drop()
    pre_meta.tables['vm_storage'].drop()
    pre_meta.tables['vmware'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['api'].create()
    pre_meta.tables['hardware'].create()
    pre_meta.tables['idrac'].create()
    pre_meta.tables['node'].create()
    pre_meta.tables['sio_volume'].create()
    pre_meta.tables['user'].create()
    pre_meta.tables['vm_host'].create()
    pre_meta.tables['vm_storage'].create()
    pre_meta.tables['vmware'].create()
