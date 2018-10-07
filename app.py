import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient
from bs4 import BeautifulSoup


class AdminHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("This is the admin page placeholder...")


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(
            '<html><body><form action="/" method="POST">'
            '<input type="text" name="message">'
            '<input type="submit" value="Submit">'
            '</form></body></html>'
        )

    async def post(self):
        http = AsyncHTTPClient()
        url = self.get_body_argument("message")
        response = await http.fetch(url)
        soup = BeautifulSoup(response.body, 'html.parser')
        self.write("Fetched " + str(len(response.body)) + " characters from" + url + soup.get_text())


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/admin", AdminHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
