from xmlrpc import client

url='https://eneasarmas-odoo-curso-curso-2928959.dev.odoo.com/'
db='eneasarmas-odoo-curso-curso-2928959'
username='admin'
password='admin'

common = client.ServerProxy("{}/rpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)