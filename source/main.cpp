#include "types.h"
#include "app/lua_bind.h"
#include "lib/l2c_imports.h"
#include "useful/const_value_table.h"
#include "useful/crc32.h"
#include "acmd_wrapper.h"
#include "useful/raygun_printer.h"

namespace skyline::TcpLogger{
    void LogFormat(const char *format, ...);
}
u64 APP_TEXT;
u64 APP_RODATA;

extern "C" {
    void *__dso_handle; // for linking with libc++
    void A64HookFunction(void *const symbol, void *const replace, void **result);
}

extern "C" void pluginMain() {
    skyline::TcpLogger::LogFormat("Hello world from plugin~!");

    // Do your hooking here, etc
    
    // A64HookFunction(
    //     reinterpret_cast<void*>(),
    //     reinterpret_cast<void*>(),
    //     reinterpret_cast<void**>()
    // )

}