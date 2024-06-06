//
// Created by user064 on 06.06.24.
//

#include "SmartPtr.h"

namespace cllt {
    SmartPtr::SmartPtr(): obj(nullptr) {}

    SmartPtr::SmartPtr(int *obj): obj(obj) {}

    void SmartPtr::init(int *obj){
        this->obj = obj;
    }

    int *SmartPtr::enter() const {
        return obj;
    }

    void SmartPtr::exit()
    {
        delete obj;
    }
} // cllt