//
// Created by user064 on 06.06.24.
//

#ifndef PYLLT_SMARTPTR_H
#define PYLLT_SMARTPTR_H

#include <exception>

namespace cllt {

    class SmartPtr {
    public:
        /**
         * A smart pointer class.
         */
        SmartPtr();

        explicit SmartPtr(int* obj);

        /**
         * Initialize the smart pointer.
         * @param obj The object to be managed.
         */
        void init(int* obj);


        /**
         * Enter the context.
         * @return The object.
         */
        int* enter() const;


        /**
         * Exit the context.
         */
        void exit();


    private:
        int* obj;
    };

} // cllt

#endif //PYLLT_SMARTPTR_H
