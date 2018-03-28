Constraints
===========

Could setup a syntax like OpenEdX's JSON has:

```json
"CODE_JAIL": {
  "limits": {
    "CPU": 1,
    "FSIZE": 1048576,
    "PROXY": 0,
    "REALTIME": 3,
    "VMEM": 536870912
  },
  "python_bin": "/edx/app/edxapp/venvs/edxapp-sandbox/bin/python",
  "user": "sandbox"
}
```

It being called "CODE_JAIL" implies that it can work in cgroups, with Docker [which uses `cgroups` and `namespaces`], in FreeBSD jails, Solaris zones &etc.

Not a bad idea?
