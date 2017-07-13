#include <iostream>

class Empty {
public:
    // default constructor
    // - behaviour: 1. call each member's constructor. 2. call parent constructor. 3. call this constructor.
    // - tips: use initializer-list to optimize step-1.
    Empty() {}

    // copy constructor
    // - invoke by: Empty p2(p1); Empty p2 = p1; f(Empty p);
    // - default behaviour: bitwise copy=shallow copy.
    // - tips: require override for 1. pointer member. 2. resource management.
    Empty(const Empty &rhs) {
        std::cout << "copy constructor.\n";
    }

    // move constructor since c++11
    Empty(Empty &&rhs) {
        std::cout << "move constructor.\n";
    }

    // destructor: call each member's destructor.
    ~Empty() {}

    // operator=
    // - default behaviour: bitwise copy=shallow copy.
    // - tips: require override for 1. pointer member. 2. resource management.
    Empty &operator=(const Empty &rhs) {
        std::cout << "operator=.\n";

        if (this != &rhs) {
            // 1. call parent's operator=
            // 2. assign each member
        }

        return *this;
    }

    // move operator= since c++11
    Empty &operator=(Empty &&rhs) {
        std::cout << "move operator=.\n";
    }
};

int main() {
    auto f = [](Empty e) {};
    auto f2 = []() {return Empty();};

    Empty e1; // default constructor

    Empty e2(e1); // copy constructor
    Empty e3 = e1; // copy constructor
    f(e3); // copy constructor

//    Empty e4(f2()); // move constructor not called?
    Empty e5 = std::move(e1); // move constructor

    e5 = e3; // operator=
    e5 = Empty(); // move operator=

    return 0;
}