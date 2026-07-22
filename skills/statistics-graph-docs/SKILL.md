---
name: statistics-graph-docs
description: Use this skill to assist the agent in visualizing datasets by generating graphs when the student requests it.
---

# statistics-graph-docs

## Overview
This skill provides the agent with the ability to show visual data to the student. Visualizing data helps students understand statistical distributions intuitively.

## Instructions

1. When a student successfully answers a statistics quiz, the agent will ask if they want to see a visual graph of the dataset.
2. Evaluate the student's natural language response:
   - If the student agrees (e.g., "yes", "sure", "of course", "I want to see"), you MUST execute the `generate_graph` tool using the dataset provided in the context.
   - If the student declines (e.g., "no", "skip", "nah"), politely acknowledge their choice and let them proceed.
3. After executing the tool, tell the student briefly: "I have generated the graph for you! Please close the graph window when you are ready to continue."