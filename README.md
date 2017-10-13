# python_web
廖雪峰python实战练习，顺便做笔记
## day1-day3
### 创建文件目录
```
python_web
	-backup
	-conf
	-www
		-static
		-templates
```

### 编写app骨架
在www文件夹中编写一个app.py, 使用aiohttp框架
注意：在廖雪峰的给出的代码中, response没有给出content参数，所以是下载一个纯文本文件，应该将content_type参数设置为：```content_type='text/html'```

### 编写ORM
我们要首先把常用的SELECT、INSERT、UPDATE和DELETE操作用函数封装起来。
由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步IO操作，因为所有用户都是由一个线程服务的，协程的执行速度必须非常快，才能处理大量用户的请求。而耗时的IO操作不能在协程中以同步的方式调用，否则，等待一个IO操作时，系统无法响应任何其他用户。

这就是异步编程的一个原则：一旦决定使用异步，则系统每一层都必须是异步，“开弓没有回头箭”。

幸运的是aiomysql为MySQL数据库提供了异步IO的驱动。

#### 创建连接池
创建一个全局的连接池，每个HTTP请求都可以从连接池中直接获取数据库连接。使用连接池的好处是不必频繁地打开和关闭数据库连接，而是能复用就尽量复用。

由于教程还是比较难懂，因此直接复制看代码即可