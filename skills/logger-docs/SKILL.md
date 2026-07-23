---
name: logger-docs
description: Use this skill to complement automatic session logging. Instructs the agent when and how to use the write_log tool for recording system events and educational milestones into dialogue_history.txt.
---

# logger-docs

## Overview
This skill guides the agent on actively recording critical learning events, system statuses, and exercise milestones in coordination with the background Python logger.

## Instructions

### 1. When to Call `write_log` Tool
You have access to the `write_log` tool. You SHOULD call it with `role="SYSTEM"` in the following scenarios:
* **Quiz Generation**: Whenever you generate a new word problem for the student, call `write_log(role="SYSTEM", text="Generated Problem: <problem text>")`.
* **Evaluation Result**: Right after validating a student's numeric answer, call `write_log(role="SYSTEM", text="Evaluation: <CORRECT/WRONG> for answer <student answer>")`.
* **Topic Transition**: When guiding the student back to `main.py` or switching topics, call `write_log(role="SYSTEM", text="Switching topic or returning to main menu.")`.

### 2. Formatting Rules
* Always ensure the `role` parameter is set to `"SYSTEM"` when recording agent-driven system logs.
* Keep the logged text clear, structured, and informative.