import threading
import asyncio

@asyncio.coroutine
def hello(id):
    print('func {}: Hello world! {}'.format(id, threading.currentThread()))
    # 模拟IO操作，协程执行
    yield from asyncio.sleep(5)
    print('func {}: Goodbye world! {}'.format(id, threading.currentThread()))


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


def demo1():
    loop = asyncio.get_event_loop()
    tasks = [hello(1), hello(2)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


def demo2():
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()  

#代码参考:https://www.liaoxuefeng.com/wiki/1016959663602400/1017970488768640
if __name__ == '__main__':
    #demo1()
    demo2()
    

 