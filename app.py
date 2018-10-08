import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient
import tornado_mysql

from internal import generate_html_word_cloud


class AdminHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("This is the admin page placeholder...")


class MainHandler(tornado.web.RequestHandler):

    def get(self):

        conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='word_tornado')
        cur = conn.cursor()
        # yield cur.execute("SELECT Host,User FROM user")
        # print(cur.description)
        # for row in cur:
        #     print(row)
        cur.close()
        conn.close()

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
        html = generate_html_word_cloud(response=response)
        self.write(html)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/admin", AdminHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
