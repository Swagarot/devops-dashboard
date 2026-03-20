# devops-dashboard
learning devops
SSH authentication enabled
DevOps Dashboard (Python CLI)

devops-dashboard is a lightweight, menu-driven Python CLI that groups a few common “ops helper” utilities into one place.

Features

    System Info: Displays basic host/user context including hostname, current username, and current working directory.
    Log Checker: Prompts for a log file path and prints any lines containing "ERROR". Includes basic error handling for missing files and unexpected exceptions.
    Task List: Simple in-memory task manager to add tasks, view tasks, and remove tasks by number during the current session.

How it works Running main.py starts an interactive loop and lets you choose between:

    System Info
    Log Checker
    Task List
    Exit

Project structure

    main.py — CLI menu / dispatcher
    sysinfo.py — system information helper
    logcheck.py — log scanning helper (filters lines containing ERROR)
    tasklist.py — interactive task manager
