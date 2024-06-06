//
// Created by user064 on 06.06.24.
//

#include <stdexcept>
#include <utility>
#include "CallbackFactory.h"

namespace cllt {
    void CallbackFactory::registerCallback(const std::string& event, std::function<void()> callback) {
        creators[event] = std::move(callback);
    }

    void CallbackFactory::create(const std::string &event) {
        if (creators.find(event) != creators.end()) {
            creators[event]();
        } else {
            throw std::invalid_argument("Event " + event + " not registered");
        }
    }
} // cllt