{
    "target_defaults": {
      "defines": [
        "NDEBUG",
        "FRONTEND",
        "_REENTRANT",
        "_THREAD_SAFE",
        "_POSIX_PTHREAD_SEMANTICS",
        "UNSAFE_STAT_OK",
      ],
      "include_dirs": [
        ".",
        "bklib",
        "libpq",
        "build/include",
        "<(node_root_dir)/deps/openssl/openssl/include",
        "/opt/local/include",
        "<!(node -e \"require('nan')\")"
      ]
    },
    "targets": [
    {
      "target_name": "binding",
      "libraries": [
        "-L/opt/local/lib",
      ],
      "sources": [
        "binding.cpp",
        "bklib/bkjs.cpp",
        "bklib/bklib.cpp",
        "libpq/chklocale.c",
        "libpq/fe-connect.c",
        "libpq/fe-misc.c",
        "libpq/fe-protocol3.c",
        "libpq/ip.c",
        "libpq/noblock.c",
        "libpq/pqsignal.c",
        "libpq/wchar.c",
        "libpq/encnames.c",
        "libpq/fe-exec.c",
        "libpq/fe-print.c",
        "libpq/fe-secure.c",
        "libpq/libpq-events.c",
        "libpq/pgstrcasecmp.c",
        "libpq/fe-auth.c",
        "libpq/fe-lobj.c",
        "libpq/fe-protocol2.c",
        "libpq/inet_aton.c",
        "libpq/md5.c",
        "libpq/pqexpbuffer.c",
        "libpq/thread.c",
        "libpq/strlcpy.c"
      ],
      "conditions": [
        [ 'OS=="mac"', {
          "defines": [
            "OS_MACOSX",
          ],
          "xcode_settings": {
            "OTHER_CFLAGS": [
              "-g -fPIC",
            ],
          },
          "sources!": [
            "src/libpq/strlcpy.c"
          ]
        }],
        [ 'OS=="linux"', {
          "defines": [
            "OS_LINUX",
          ],
          "cflags_cc+": [
            "-g -fPIC -rdynamic",
          ],
        }],
      ]
    }]
}
