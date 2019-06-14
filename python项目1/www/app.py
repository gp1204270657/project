# coding=utf-8
import logging; logging.basicConfig(level=logging.INFO)
import asyncio
from aiohttp import web


#定义服务器返回的信息
async def index(requset):
    return web.Response(body=b'<h1>hello,dad<h1>',content_type='text/html')

#建立服务器连接，监听本地端口9000的请求，对首页‘/’进行响应
def inti():
    app=web.Application()
    app.router.add_get('/',index)
    web.run_app(app,host='127.0.0.1',port=9001)


if __name__ == '__main__':
    inti()