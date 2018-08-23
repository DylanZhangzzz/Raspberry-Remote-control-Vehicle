#!/usr/bin/python2 //by the second best Engineer in the world Dinghuang Zhang up793903
#coding=utf-8
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import urllib
import tank 
from abc import ABCMeta, abstractmethod

class splitdata(BaseHTTPRequestHandler):
        def do_GET(self):
                data= self.path.split('?', 1)
                action = data[0]
                numdata = {}
                if len(data) == 2:
                            data_value=data[1]
                            kv = data_value.split('=')
                            if len(kv) == 2:
                               numdata[kv[0]] = urllib.unquote(kv[1])
                print(data)
                print(numdata)
                TK = TankAction()
                RT = {}
                if self.path.startswith("/car?"):
                        RT["return"] = TK.action(numdata)
                else:
                        RT["return"] = -1
                self.protocal_version = "HTTP/1.1"
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=UTF-8")
                self.end_headers()
                self.wfile.write(RT)

class usercommand():
        __metaclass__ = ABCMeta
        @abstractmethod
        def action(self, numdata):
                pass
class TankAction(usercommand):
        def __init__(self):
                tank.init()
        def action(self, numdata):
                print (numdata)
                act = int(numdata['a'])
                if act == 0:
                        tank.stop()
                        return 0
                if act == 2:
                        tank.back()
                        return 0
                if act == 8:
                        tank.front_left()
                        return 0
                if act == 9:
                        tank.front_right()
                        return 0
                if act == 10:
                        tank.back_left()
                        return 0
                if act == 11:
                        tank.back_right()
                        return 0
                if act == 3:
                        tank.left_turn()
                        return 0
                if act == 4:
                        tank.right_turn()
                        return 0
                if act == 1:
                        tank.forward()
                        return 0
                if act == 5:
                        tank.turret_left_turn()
                        return 0
                if act == 6:
                        tank.turret_right_turn()
                        return 0
                if act == 7:
                        tank.shoot()
                        return 0
                if act == 12:
                        tank.gun_up()
                        return 0
                if act == 13:
                        tank.gun_down()
                        return 0
                if act == 14:
                        tank.aim_on()
                        return 0
                if act == 15:
                        tank.aim_off()
                        return 0
                else:
                        return -1

if __name__ == "__main__":
        PORT_NUM = 8899
        serverAddress = ("", PORT_NUM)
        server = HTTPServer(serverAddress, splitdata)
        server.serve_forever()
        
