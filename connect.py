import pymongo
import random
password = ""

dbname = ""

def links():
        url = "mongodb+srv://shivamsinha212:" + password + "@cluster0-3mqn5.mongodb.net/" + dbname + "?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        perBlog = client['personalblog']
        l = []
        for x in perBlog.posts.find({}):
                l.append(x)
        return l[::-1]

def myquery(pId):
        myquery = {"redirect" : str(pId)}
        url = "mongodb+srv://shivamsinha212:" + password + "@cluster0-3mqn5.mongodb.net/" + dbname + "?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        perBlog = client['personalblog']
        post = list(perBlog.posts.find(myquery))

        return post
def random_post():

        url = "mongodb+srv://shivamsinha212:" + password + "@cluster0-3mqn5.mongodb.net/" + dbname + "?retryWrites=true&w=majority"
        client = pymongo.MongoClient(url)
        perBlog = client['personalblog']
        return random.randint(1,perBlog.posts.count())
