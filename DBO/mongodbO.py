import pymongo

mongodbIP = "mongodb://192.168.1.104:27017/"
def getCollection():
    myclient = pymongo.MongoClient(mongodbIP)#("mongodb://202.194.246.155:27017/")
    mydb = myclient["monitor"]
    mycol = mydb["updateDate"]
    return mycol

def getWendujiCollection():
    myclient = pymongo.MongoClient(mongodbIP)#("mongodb://202.194.246.155:27017/")
    mydb = myclient["mydb"]
    mycol = mydb["WuDuJi"]
    return mycol

def getTDXCollection():
    myclient = pymongo.MongoClient(mongodbIP)#("mongodb://202.194.246.155:27017/")
    mydb = myclient["quantaxis"]
    mycol = mydb["stock_transaction"]
    return mycol

mycol = getCollection()

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


def insert():
    col = getCollection()

    mydict = { "date": "2020-03-13", "state":{"santai": False} }

    x = col.insert_one(mydict)
    print(x)

def find():

    x = mycol.find_one()

    print(x)

def findmany():

    myquery = {"date": {"$gt": "20200310"}}

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)

if __name__ == '__main__':
    isExist()