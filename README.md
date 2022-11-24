# awesome-coroutine
协程多语言DEMO

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
```go
// 执行一个函数
func()
// 开启一个协程执行这个函数
go func()
```


## Java

java19引入了<b>虚拟线程</b>（Virtual Thread），终于支持协程了。

新API：
* Thread.ofVirtual()：虚拟线程，也就是协程
* Thread.ofPlatform()：平台线程，也就是我们现在常用的线程

```java
// Thread.getId() from jdk19 abandoned
Runnable runnable = () -> System.out.println(Thread.currentThread().threadId());
Thread thread = Thread.ofVirtual().name("testVT").unstarted(runnable);
Thread testPT = Thread.ofPlatform().name("testPT").unstarted(runnable);
testPT.start();
```

快速创建和启动虚拟线程：
```java
Runnable runnable = () -> System.out.println(Thread.currentThread().threadId());
Thread thread = Thread.startVirtualThread(runnable);
```

`Executors.newVirtualThreadPerTaskExecutor()` 虚拟线程池：
```java
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
  executor.submit(() -> System.out.println("hello"));
}
```

> 因为虚拟线程是预览特性，需要用 `javac --release 19 --enable-preview Main.java` 编译程序，再用 `java --enable-preview Main` 运行程序
> 或者使用`java --source 19 --enable-preview Main.java`运行程序


参考：
* http://static.kancloud.cn/gofor/golang-learn/2120519
* https://medium.com/javarevisited/how-to-use-java-19-virtual-threads-c16a32bad5f7
