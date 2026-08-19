#!/usr/bin/env python3
"""Keep the Windows display + system awake while a long task runs.
Usage: python keep_awake.py [--seconds N]   (default: run until killed)
Calling SetThreadExecutionState(ES_CONTINUOUS|ES_SYSTEM_REQUIRED|ES_DISPLAY_REQUIRED)
every 60s prevents sleep + display-off. On Ctrl-C / kill, flags are cleared.
"""
import argparse, ctypes, time, sys

ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def set_state(flags):
    try:
        ctypes.windll.kernel32.SetThreadExecutionState(flags)
    except Exception as e:
        print(f"SetThreadExecutionState failed: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=int, default=0, help="run N seconds then exit (0 = until killed)")
    args = ap.parse_args()

    flags = ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED
    set_state(flags)
    print("display + system kept awake (flags set, ES_CONTINUOUS)")

    start = time.time()
    try:
        while True:
            time.sleep(60)
            set_state(flags)
            if args.seconds and time.time() - start >= args.seconds:
                break
    except KeyboardInterrupt:
        pass
    finally:
        set_state(ES_CONTINUOUS)
        print("awake flags cleared, power management restored")

if __name__ == "__main__":
    main()
