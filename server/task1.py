import tornado.ioloop
import tornado.web
from tornado import gen
from tornado import httpclient


class MainHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        http_client = httpclient.HTTPClient()
        try:
            response = http_client.fetch("https://services.drova.io/")
            self.write(str(response.code))
        except httpclient.HTTPError as e:
            self.write("Error: " + str(e))
        except Exception as e:
            self.write("Error: " + str(e))
        http_client.close()
        # self.finish()


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
