---
title: Over-Engineering, oh man...
description: Over-Engineering is a real Problem and it is not easy to catch yourself doing it, unless you are documenting at the same time. Like i was while writing issue for my project.  
date: 2025-09-21
draft: false
toc: true
ShowLastmod: true
---

## What is Over-Engineering?
This is very common process of having an issue and coming up with crazy solution that is not needed at all. that is a simper explanation of [this](https://en.wikipedia.org/wiki/Overengineering).

## How to get rid of it?
Over-Engineering is not a good thing as we see. Why waste time and energy on solution that can be simplified and that does the same thing, more efficiently. 
One time i was writing an [issue](https://github.com/demetrebadzaradze/InstaSwarm/issues/7) on GitHub where where i caught myself just going all over the place for a simple bug. 
### Simple explanation
So the bug was that application was not refreshing tokens because it didn't know when it was needed, so it would throw some error logs and keep on running with all things wrong with it.
i knew that 