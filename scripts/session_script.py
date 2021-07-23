from xmlrpc import client

url='https://eneasarmas-odoo-curso-curso-2928959.dev.odoo.com'
db='eneasarmas-odoo-curso-curso-2928959'
username='eneasaao@gmail.com'
password='q1w2e3r4'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'academy.session','check_access_rights',
                                ['write'],{'raise_exception': False})
                              
print('model_access')
print(model_access)


courses = models.execute_kw(db, uid, password,
                            'academy.course','search_read',
                            [[['level','in',['intermediate','beginner']]]])
                            
print('courses')
print(courses)
course = models.execute_kw(db, uid, password,
                            'academy.course','search',
 #                           [[['name','in',['Accounting 200','Quimic 101']]]])
                            [[['name','=','Accounting 200']]])
print('course')                            
print(course)
                            
session_fields = models.execute_kw(db, uid, password,
                            'academy.session','fields_get',
                            [],{'attributes':['string','type','required']})
                            
print('session_fields') 
print(session_fields)  
                            

new_session = models.execute_kw(db, uid, password,
                            'academy.session','create',
                            [
                                {
                                    'course_id': course[0],
                                    'state': 'open',
                                    'duration': 4,
                                }
                            ]
                            )
                            
print(new_session)