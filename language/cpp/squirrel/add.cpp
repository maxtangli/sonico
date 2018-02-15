#include <squirrel.h>
#include <sqrat.h>
#include <iostream>

/*
g++ -Wall -g -o add add.cpp -I squirrel3/include/ -I sqrat-0.8.3/include/ -L  squirrel3/lib/ -l:libsquirrel.a -l:libsqstdlib.a

http://wiki.squirrel-lang.org/mainsite/Wiki/default.aspx/SquirrelWiki/Embedding%20Getting%20Started.html
*/

int main(int argc, char* argv[])
{
    // initial
    HSQUIRRELVM vm;
    vm = sq_open(1024);

    sqstd_seterrorhandlers(vm);
    
    sq_pushroottable(vm);
    SQRESULT result = sqstd_dofile(vm, "add.cnut", SQFalse, SQTrue);
    if (SQ_FAILED(result)){
        std::cerr << "error: failed sqstd_dofile add.cnut.";
        return 1;
    }
    
    // call squirrel function by sqrat
    using namespace Sqrat;
    Function funcAdd(RootTable(vm), "add");
    if (funcAdd.IsNull()) {
        std::cerr << "error: funcAdd.IsNull();";
        return 1;
    }
    
    int a = 1, b = 1;
    int c = funcAdd.Evaluate<int>(a, b);
    std::cout << "1 + 1 = " << c << ".\n";
    funcAdd.~Function();
    
    // destroy
    sq_pop(vm, 1);
    sq_close(vm);
    return 0;
}

