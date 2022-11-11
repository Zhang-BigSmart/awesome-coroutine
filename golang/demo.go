package main

import (
	"bytes"
	"fmt"
	"os"
	"runtime"
	"strconv"
	"time"
)

//编写一个函数，每隔一秒输出 "hello,world"
func test(id int) {
	for i := 1; i <= 10; i++ {
		fmt.Printf("func %d hello,world - pid: %v gid: %v - count: %s\n", id, os.Getpid(), getGID(), strconv.Itoa(i))
		time.Sleep(time.Second)
	}
}

func main() {

	go test(1) //开启了一个协程，使其同时执行
	go test(2)
	time.Sleep(10 * time.Second)
}

// 获取协程ID（不建议使用）
func getGID() uint64 {
	b := make([]byte, 64)
	b = b[:runtime.Stack(b, false)]
	b = bytes.TrimPrefix(b, []byte("goroutine "))
	b = b[:bytes.IndexByte(b, ' ')]
	n, _ := strconv.ParseUint(string(b), 10, 64)
	return n
}
