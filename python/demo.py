# 在Python中有多种方式可以实现协程，例如：
# greenlet，是一个第三方模块，用于实现协程代码（Gevent协程就是基于greenlet实现）
# yield，生成器，借助生成器的特点也可以实现协程代码。
# asyncio，在Python3.4中引入的模块用于编写协程代码。
# async & awiat，在Python3.5中引入的两个关键字，结合asyncio模块可以更方便的编写协程代码。
# 说实话我在各大博客，论坛见到的各式各样，总结下来其实也就这几种

# greenlet,早期模块
# yield关键字.
# asyncio 装饰器(py3.4)
# async , await 关键字(py3.5)[推荐]

import asyncio


async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))