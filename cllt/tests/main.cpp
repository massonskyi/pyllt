//
// Created by user064 on 06.06.24.
//
#include "cllt/CallbackFactory.h"
#include "cllt/TimeitPtr.h"
#include "cllt/SmartPtr.h"
#include <iostream>
#include <thread>

void print(const std::string& message){
    std::cout  << message << std::endl;
}

class MyClass {
public:
    explicit MyClass(int value) : value(value) {}

    int getValue() const {
        return value;
    }

private:
    int value;
};
int main() {
    cllt::TimeitPtr timer;
    cllt::CallbackFactory factory;
    timer.run();

    factory.registerCallback("start", [](){
        print( "sss"); // Вызов функции printFunction с аргументом "sss"
    });

    factory.registerCallback("stop", [](){
        print("zzz"); // Вызов функции printFunction с аргументом "sss"
    });

    try {
        factory.create("start");
    } catch (const std::invalid_argument& e) {
        std::cerr << e.what() << std::endl;
    }
    timer.stop();

    std::cout << timer << std::endl;

    auto my_function_timed = cllt::TimeitPtr::timeit([&factory](){
        factory.create("stop");
    });
    my_function_timed();
    std::cout << std::endl;  // Выведет "Elapsed time is 1.0 s"

    auto* myClass = new MyClass(10);
    cllt::SmartPtr smartPtr;
    smartPtr.init(reinterpret_cast<int *>(myClass));
    const auto* obj = reinterpret_cast<const MyClass *>(smartPtr.enter());
    std::cout << obj->getValue() << std::endl;  // Output: 10
    smartPtr.exit();
    return 0;
}