---
title: README.md
description: README from github
date: 2025-01-15
draft: false
toc: true
ShowLastmod: true
---

# Second Brain
 **Second Brain is a blog** witch lives on GitHub and posts can be added though git.
 ### How does it work
  Base of this site is [Hugo](https://gohugo.io/) witch I use to turn `.md` files into `Html`'s and with help of theme [Hermit-v2](https://themes.gohugo.io/themes/hermit-v2/) I didn't have to write any html/CSS or JavaScript  and all of that made this beautiful [site](https://demetrebadzaradze.github.io/Second-Brain/en/) .
  Next was moving that to git for living, so I wont have to modify and tweak master branch manually or even build over and over again for that I have 3 different branches `master`, `posts`, `For-Hosting` witch have different proposes.
  - `master` contain whole thing , that also where building site happens.
  - `posts` is mostly clear branch but I might change that to contain all posts but what it does RN is with GitHub action when someone pushes to that branch, it moves every `.md` files to master branch in `content/Posts`, and then gets cleared.
  - `For-Hosting` is what name suggests and it contains `public` folder from `master` witch is already built site 
  ### How can you use it??
   coming soon.
  ### what I'm planning to do
  1. this site will contain things I do in programing, so it will be portfolio like.
  2. I also am tryna make this as factionless as possible for other less experienced people to use and for me to, like I don't want to resolve merge conflict hen I just want to write so here are some ideas for this:
	  - **obsidian extension**
		  I use obsidian for note taking and I also will for writing this posts because it simple and  I can mod it to add publishing from the obsidian so no terminal or web needed for that.  
	 - **usable for many OS** 
		 currently it only works on my windows machine but I will try to make it for other people too if someone needs.
	  - **some posts ideas **
		   1. home server stuff.
		   2. deep dive on how does this site works.
		   3. and I need to make list for future projects too.
