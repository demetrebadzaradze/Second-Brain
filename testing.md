---
title: testinn whole site
date: 2025-01-13
description : this site is hosted on github and i have some CI/CD stuff and this is testing it. so, is it working?? 
toc : true
ShowLastmod : true
---

### how does it works
i am so tired,
i made posts branch that is clear and gets cleared every time someone pushes to it with workflow that:
1. copies all .md files from posts branch into master
1. build site with hugo+hermit-v2 and updates repo
1. then takes `public` dir and copies it to `For-Hosting` branch
1. and the github pages workflow is beeng runed and site is beeng published

#### i will be updating this file about how things work in here, and some future stuff that i will be doing on this site.