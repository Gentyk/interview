from tornado.ioloop import IOLoop
import tornado.httpserver
import aiohttp
import requests
import tornado.web
import tornado.ioloop
import asyncio


async def req():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://services.drova.io/') as resp:
            return resp.status


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        result = asyncio.run(req())
        self.write(str(result))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()