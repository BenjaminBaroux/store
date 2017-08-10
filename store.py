from bottle import route, run, template, static_file, get, post, delete, request
import json
import pymysql

connection = pymysql.connect(host='sql11.freesqldatabase.com',
                             user='sql11189252',
                             password='ELN2mAfWdj',
                             db='sql11189252',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

@get("/admin")
def admin_portal():
	return template("pages/admin.html")

# list categories
@get('/categories')
def list_of_categories():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, name from categories;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps ({"STATUS": "SUCCESS",
                                "CATEGORIES": result,
                                "CODE":"200"})

    except Exception:
        return json.dumps({"STATUS": "INTERNAL ERROR",
                           "MSG": "There was an internal error",
                           "CODE": "500"})

# list products in each categories
@get('/category/<id>/products')
def get_products(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from Products WHERE category = {0};".format(str(id))
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({"STATUS": "SUCCESS",
                               "PRODUCTS": result,
                               "CODE":"200"})
    except Exception:
        return json.dumps({"STATUS": "INTERNAL ERROR",
                           "MSG": "There was an internal error",
                           "CODE": "500"})
# list products
@get('/products')
def list_product():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from Products;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({"STATUS": "SUCCESS",
                               "PRODUCTS": result,
                               "CODE":"200"})
    except Exception:
        return json.dumps({"STATUS": "INTERNAL ERROR",
                           "MSG": "There was an internal error",
                           "CODE": "500"})

@get('/product/<id>')
def get_product(id):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * from Products WHERE id = {0};".format(str(id))
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({"STATUS": "SUCCESS",
                               "PRODUCTS": result,
                               "CODE":"200"})
    except Exception:
        return json.dumps({"STATUS": "INTERNAL ERROR",
                           "MSG": "There was an internal error",
                           "CODE": "500"})

#delete category
@delete('/category/<id>')
def delete_category(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE from categories WHERE id = {0}".format(id)
            cursor.execute(sql)
            connection.commit()
            return json.dumps({"STATUS": "SUCCESS",
                               "CODE":"201"})
    except Exception:
        return json.dumps({"STATUS": "INTERNAL ERROR",
                           "MSG": "There was an internal error",
                           "CODE": "500"})

#delete product
@delete('/product/<id>')
def delete_product(id):
    try:
        with connection.cursor() as cursor:
            sql = "DELETE from Products WHERE id = {0};".format(id)
            cursor.execute(sql)
            connection.commit()
            return json.dumps({"STATUS": "SUCCESS",
                               "PRODUCTS": result,
                               "CODE":"201"})
    except Exception:
        return json.dumps({"STATUS": "INTERNAL ERROR",
                           "MSG": "There was an internal error",
                           "CODE": "500"})


#add category
@post('/category')
def add_categories():
    try:
        with connection.cursor() as cursor:
            name = request.POST.get("name")
            sql = "INSERT INTO categories VALUES (0, '{}')".format(name)
            cursor.execute(sql)
            connection.commit()
            return json.dumps ({"STATUS": "SUCCESS",
                                "CODE":"201"})

    except Exception:
        return json.dumps({"STATUS": "INTERNAL ERROR",
                           "MSG": "There was an internal error",
                           "CODE": "500"})

#add product & update product
@post('/product')
def add_product():
    category = request.POST.get("category")
    description = request.POST.get("desc")
    price = request.POST.get("price")
    title = request.POST.get("title")
    favorite = request.POST.get("favorite")
    if favorite:
        fav = True
    else:
        fav = False
    image = request.POST.get("img_url")
    try:
        with connection.cursor() as cursor:
            sql = "SELECT COUNT(*) FROM Products WHERE title = '{}'".format(title)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result['COUNT(*)'] > 0:
                sql_update = "UPDATE Products SET category={0}, description='{1}', price= {2}, favorite={3}, img_url= '{4}' WHERE title='{5}'".format(category,description,price,fav,image,title)
                print(sql_update)
                cursor.execute(sql_update)
                product_ID = 0
                connection.commit()
            else:
                sql_add = "INSERT INTO Products VALUES (id,{0},'{1}',{2},'{3}',{4},'{5}')".format(category,description,price,title,fav,image)
                cursor.execute(sql_add)
                product_ID = cursor.lastrowid
                connection.commit()
        return json.dumps({"STATUS": "SUCCESS",
                               "PRODUCT_ID": product_ID,
                               "CODE": "201"})
    except Exception:
        return json.dumps({"STATUS": "INTERNAL ERROR",
                           "MSG": "There was an internal error",
                           "CODE": "500"})
@get("/")
def index():
    return template("index.html")

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')

@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')

run(host='localhost', port=8000)
