# import orm
# from models import User, Blog, Comment

# def test():
#     yield from orm.create_pool(user='root', password='1234', database='awesome')

#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

#     yield from u.save()

# for x in test():
#     pass



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Max'  #作者
__date__ = "2017/9/10 14:41"  #创建时间

import orm, asyncio
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='1234', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()