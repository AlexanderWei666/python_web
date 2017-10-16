# import orm
# from models import User, Blog, Comment

# def test():
#     yield from orm.create_pool(user='root', password='1234', database='awesome')

#     u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
#     u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')
#     u = User(name='Test3', email='test3@example.com', passwd='1234567890', image='about:blank')
#     u = User(name='Test4', email='test4@example.com', passwd='1234567890', image='about:blank')

#     yield from u.save()

# for x in test():
#     pass



#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# __author__ = 'Max'  #作者
# __date__ = "2017/9/10 14:41"  #创建时间

import orm, asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='1234', db='awesome')
    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
    u1 = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')
    u2 = User(name='Test3', email='test3@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    await u1.save()
    await u2.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()

# # test mvc
# @get('/')
# def index(request):
#     users = yield from User.findAll()
#     return {
#         '__template__': 'test.html',
#         'users': users
#     }