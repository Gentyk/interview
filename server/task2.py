from tornado.ioloop import IOLoop
import tornado.httpserver
import aiohttp
import tornado.web
import tornado.ioloop
import asyncio
import requests


async def req():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://services.drova.io/") as resp:
            return resp.status


def req2():
    resp = requests.get("https://services.drova.io/session-manager/version")
    return resp


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        # first version
        # result = await req()
        # self.write(str(result))

        # second version
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, req2)
        self.write(result.content)


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
