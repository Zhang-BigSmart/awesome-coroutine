package main

import (
	"fmt"
	"strconv"
	"time"
)

//编写一个函数，每隔一秒输出 "hello,world"
func test() {
	for i := 1; i <= 10; i++ {
		fmt.Println("test hello,world " + strconv.Itoa(i))
		time.Sleep(time.Second)
	}
}
func main() {

	go test() //开启了一个协程，使其同时执行
	for i := 1; i <= 10; i++ {
		fmt.Println("mian() hello,world " + strconv.Itoa(i))
		time.Sleep(time.Second)
	}
}
