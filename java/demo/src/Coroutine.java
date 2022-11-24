import java.time.Duration;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

/**
 * @author : zzh
 * create at:  2022/11/19
 */
public class Coroutine {





    public static void main(String[] args) throws InterruptedException {

        // 快速创建和启动一个虚拟线程
        var vThread = Thread.startVirtualThread(() -> {
            System.out.println("Hello from the virtual threadId:" + Thread.currentThread().threadId());
        });

        // 等待虚拟线程结束
        vThread.join();


        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
            executor.submit(() -> System.out.println("hello"));
        }

        // 虚拟线程池
        try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
            // 循环10000次
            IntStream.range(0, 100).forEach(i -> {
                executor.submit(() -> {
                    Thread.sleep(Duration.ofSeconds(1));
                    // 协程ID
                    System.out.println("Thread ID:" + Thread.currentThread().threadId());
                    return i;
                });
            });
        }
    }
}
