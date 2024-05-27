from typing import Optional, Awaitable

import tornado.ioloop
import tornado.websocket
import tornado.web
import time

class WebsocketHandler(tornado.websocket.WebSocketHandler):
    def open(self, *args: str, **kwargs: str) -> Optional[Awaitable[None]]:
        print ('Connection Open Successfully')
        #timer to send data once per second
        self.timer = tornado.ioloop.PeriodicCallback(self.send_data, 100)
        self.timer.start()

    def on_close(self) -> None:
        print("Stopping The connection")
        self.timer.stop()

    def send_data(self):
        self.write_message('Now it is: ' + str(time.time()))

websocket = tornado.web.Application([(r'/', WebsocketHandler),])

if __name__ == '__main__':
    websocket.listen(2323)
    tornado.ioloop.IOLoop.instance().start()

