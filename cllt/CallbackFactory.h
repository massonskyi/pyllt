//
// Created by user064 on 06.06.24.
//

#ifndef CLLT_CALLBACKFACTORY_H
#define CLLT_CALLBACKFACTORY_H

#include <string>
#include <functional>
#include <unordered_map>

namespace cllt {

    class CallbackFactory {
    public:
        CallbackFactory() = default;

        ~CallbackFactory() = default;
        void registerCallback(const std::string& event, std::function<void()> callback);
        void create(const std::string& event);

    private:
        std::unordered_map<std::string, std::function<void()>> creators;
    };

} // callbacks

#endif //CLLT_CALLBACKFACTORY_H
