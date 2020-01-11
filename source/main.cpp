#include "main.hpp"
#include "types.h"

extern "C" {
    void *__dso_handle; // for linking with libc++
    void A64HookFunction(void *const symbol, void *const replace, void **result);
}

extern "C" void pluginMain(void) {

}