import pymongo

def creatDB():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["monitor"]

def isExist():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    dblist = myclient.list_database_names()
    # dblist = myclient.database_names()
    if "monitor" in dblist:
        print("数据库已存在！")
    else:
        print('no')

def creatCollection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["monitor"]

    mycol = mydb["updateDate"]

def isCollectionExist():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')

    mydb = myclient['monitor']

    collist = mydb.list_collection_names()
    # collist = mydb.collection_names()
    if "sites" in collist:  # 判断 sites 集合是否存在
        print("集合已存在！")

def getCollection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["monitor"]
    mycol = mydb["updateDate"]
    return mycol
def insert():
    col = getCollection()

    mydict = {"name": "santai", "date": "20200312", "isupdate": False}

    x = col.insert_one(mydict)
    print(x)

def find():
    mycol = getCollection()
    x = mycol.find_one()

    print(x)

if __name__ == '__main__':
    find() 