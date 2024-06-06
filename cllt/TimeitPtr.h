//
// Created by user064 on 06.06.24.
//

#ifndef CLLT_TIMEPTR_H
#define CLLT_TIMEPTR_H

#include <functional>
#include <chrono>
#include <utility>
#include <ostream>

namespace cllt {
    class TimeitPtr {
    public:
        explicit TimeitPtr(std::function<double()> f = [](){
            return std::chrono::duration_cast<std::chrono::duration<double>>(std::chrono::steady_clock::now().time_since_epoch()).count();
        }, double t=0.0) : t(t), f(std::move(f)) {}

        void run();
        void stop();

        friend std::ostream& operator<<(std::ostream& os, const TimeitPtr& timer);
        static std::function<void()> timeit(std::function<void()> func);

    private:
        double t;
        std::function<double()> f;
        std::chrono::time_point<std::chrono::steady_clock> start;
    };

}
#endif //CLLT_TIMEPTR_H
