# awesome-coroutine
协程多语言DEMO实现

python3.7.4

## Python
在 python3.4 之前，使用三方库实现，比如：
* Gevent

3.4之后官方内置了 asyncio 标准库，真正支持协程特性
* asynico + yield from（python3.4）
* asynico + await（python3.5）【推荐】


而Python对协程的支持，是通过Generator实现的，协程是遵循某些规则的生成器。因此，我们在了解协程之前，我们先要学习生成器。

参考：廖雪峰https://www.liaoxuefeng.com/wiki/1016959663602400/1017970488768640


## Golang

Go 语言，从语言层面天生支持并发，可以说是为并发而生的语言。
用法相比于python来说，更为简洁方便
```golang
// 执行一个函数
func()
// 开启一个协程执行这个函数
go func()
```






参考：http://static.kancloud.cn/gofor/golang-learn/2120519