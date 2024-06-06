//
// Created by user064 on 06.06.24.
//

#include <iostream>
#include "TimeitPtr.h"
namespace cllt {

    void TimeitPtr::run() {
        start = std::chrono::steady_clock::now();
    }

    void TimeitPtr::stop() {
        auto end = std::chrono::steady_clock::now();
        double dt = std::chrono::duration_cast<std::chrono::duration<double>>(end - start).count();
        t += dt;
    }

    std::ostream &operator<<(std::ostream &os, const TimeitPtr &timer) {
            os << "Elapsed time is " << timer.t << " s";
            return os;
    }

    std::function<void()> TimeitPtr::timeit(std::function<void()> func) {
        return [=]() {
            auto start_time = std::chrono::steady_clock::now();
            func();
            auto end_time = std::chrono::steady_clock::now();
            double elapsed_time = std::chrono::duration_cast<std::chrono::duration<double>>(end_time - start_time).count();
            std::cout << "Function executed in " << elapsed_time << " seconds" << std::endl;
        };
    }

}