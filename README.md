# Simple Keylogger in Python

This is a simple keylogger program written in Python that records keystrokes and logs them to a file. It includes features such as daily log file rotation, timestamping for each key press, and a key press counter.

## Features

- Logs keystrokes to a new file each day (e.g., `keylog_YYYY-MM-DD.txt`).
- Records timestamps for each key press.
- Counts the total number of key presses during the logging session.
- Handles special keys appropriately.

## Requirements

- Python 3.4 or above
- `pynput` library

### Installation

To install the necessary library, use pip:

```bash
pip install pynput
