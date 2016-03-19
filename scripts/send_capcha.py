import time
from antigate import AntiGate            # AntiCaptcha

n = 1
while n<8:
    start = time.clock()
   # print AntiGate('888fe7041b163b35255dddafe49bfe6c', "/home/myroslav/reserv/reserv/visareserv/screenshot/res/%d.png" % n) # AntiCaptcha('API-KEY', 'captcha.jpg')
    print "n = %d" %n
    gate = AntiGate('888fe7041b163b35255dddafe49bfe6c')               # AntiCaptcha('API-KEY')
    captcha_id = gate.send("/home/myroslav/reserv/reserv/visareserv/screenshot/res/%d.png" % n)
    print gate.get(captcha_id)
    end = time.clock()
    n+=1
    interval = end - start
    print "interval =", interval