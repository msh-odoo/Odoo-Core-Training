import xmlrpc.client


# info = xmlrpc.client.ServerProxy('http://localhost:8069/start').start()
# url, db, username, password = info['host'], info['database'], info['user'], info['password']

# print ("\n\ninfo is ::: ", url, db, username, password)

db = "odoo15"
username = "admin"
password = "a"

common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

if uid:
    print ("Connection Successful")

models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')

# models.execute_kw(db, uid, password, 'course.course', 'create', [{'name': 'Statistics', 'state': 'new'}])

to_confrim_ids = models.execute_kw(db, uid, password, 'course.course', 'search', [[('name', '=', 'Physics')]])
print ("\n\nto_confrim_id ::: ", to_confrim_ids)

result = models.execute_kw(db, uid, password, 'course.course', 'action_confirm', [to_confrim_ids])

result = models.execute_kw(db, uid, password, 'course.course', 'search_read', [[], ['name', 'description', 'state']])

print ("\n\nresult is ::: ", result)