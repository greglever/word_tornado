# TODO(Greg): Get this running locally (or via docker-compose) in python 3
# TODO(Greg): Find the python3.6 docker image
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    # def get(self):
    #     self.write("Hello, world")

    # TODO(Greg): Run this locally
    def get(self):
        self.write('<html><body><form action="/myform" method="POST">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")

        self.write("You wrote " + self.get_body_argument("message"))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
