---
title: fun git procedure
description: see history of git and what it actually means. 
date: 2025-04-05
	draft: false
toc: true
ShowLastmod: true
---
## fun git procedure

clone the git repo (might take a While)

```bash
git clone https://github.com/git/git.git
```

get into it  and check it out. it the same one on the [git on Github](https://github.com/git/git)

```bash
cd git
ls
```

see the most important commits or the starting points of git

```bash
git rev-list --max-parents=0 HEAD
```

get the last one witch is actually the first one and checkout that commit

```bash
git checkout e83c5163316f89bfbde7d9ab23ca2e25604af290
```

and see its legendary message from [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) the creator of Linux kernel and git from 2005

```bash
git log
```

also see how small the project was back in a day and quick look at the README.md file and observe what creator describes his creation as

```bash
notepad README.md
```

or just `cat` it on Linux or `nano`