import threading
import asyncio

async def hello(id):
    print('func {}: Hello world! {}'.format(id, threading.currentThread()))
    # 模拟IO操作，协程执行
    await asyncio.sleep(5)
    print('func {}: Goodbye world! {}'.format(id, threading.currentThread()))


def demo1():
    loop = asyncio.get_event_loop()
    tasks = [hello(1), hello(2)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

#代码参考：https://www.liaoxuefeng.com/wiki/1016959663602400/1048430311230688
if __name__ == '__main__':
    demo1()
    

 