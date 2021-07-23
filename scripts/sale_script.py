from xmlrpc import client

url='https://eneasarmas-odoo-curso-curso-2928959.dev.odoo.com'
db='eneasarmas-odoo-curso-curso-2928959'
username='eneasaao@gmail.com'
password='q1w2e3r4'

common = client.ServerProxy("{}/rpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password
                                ,'sale.order','check_access_rights'
                                ,['write'],{'raise_exception':False}
                                )
print(model_access)

draft_quotes = models.execute_kw(db, uid, password
                                ,'sale.order','search'
                                ,[[['state','=','draft']]]
                                )
print(draft_quotes)

if_confirmed  = models.execute_kw(db, uid, password
                                ,'sale.order','action_confirm'
                                ,[draft_quotes]
                                )
print(if_confirmed)

