from django.db import connection


class UserService:

    def nextPk(self):
        pk = 0
        with connection.cursor() as cursor:
            sql = "select max(id) from sos_user"
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        return pk + 1

    def add(self, data):
        f = data['fullName']
        r = data['rollNo']
        p = data['physics']
        c = data['chemistry']
        m = data['maths']


        sql = "insert into sos_user values((%s), (%s), (%s), (%s), (%s))"
        data = [UserService.nextPk(self), f, r, p, c, m]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def update(self, data):
        f = data['fullName']
        r = data['rollNo']
        p = data['physics']
        c = data['chemistry']
        m = data['maths']

        sql = "update sos_marksheet set fullName = (%s), rollNo = (%s), physics = (%s), chemistry = (%s), maths = (%s)"
        data = [f, r, p, c, m]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def delete(self, id):
        sql = "delete from sos_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def auth(self, loginId, password):
        sql = "select * from sos_user where loginId = (%s) and password = (%s)"
        data = [loginId, password]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName =  ("fullName", "rollNo", "physics", "chemistry", "maths")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get(self, id):
        sql = "select * from sos_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName =  ("fullName", "rollNo", "physics", "chemistry", "maths")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def findByLogin(self, loginId):
        sql = "select * from sos_user where loginId = (%s)"
        data = [loginId]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("fullName", "rollNo", "physics", "chemistry", "maths")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def search(self, params):
        fname = params.get("fullName", "")
        pageNo = params.get("pageNo", 0)
        pageSize = params.get("pageSize", 0)
        sql = "select * from sos_user where 1=1"
        if fname != "":
            sql += " and fullName like '" + fname + "%%' "
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit %s, %s"
        print('sql => ', sql)
        cursor = connection.cursor()
        cursor.execute(sql, [pageNo, pageSize])
        result = cursor.fetchall()
        columnName =  ("fullName", "rollNo", "physics", "chemistry", "maths")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res