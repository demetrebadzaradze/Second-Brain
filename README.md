---
title: README.md
description: README from github
date: 2025-01-15
draft: false
toc: true
ShowLastmod: true
---

# Second Brain
 **Second Brain is a blog** witch lives on GitHub and posts can be added though git. it is also intended to be used with [obsidian](https://obsidian.md/).
 
 ### How does it work
  Base of this site is [Hugo](https://gohugo.io/) witch I use to turn `.md` files into `Html`'s and with help of theme [Hermit-v2](https://themes.gohugo.io/themes/hermit-v2/) I didn't have to write any html/CSS or JavaScript  and all of that made this beautiful [site](https://demetrebadzaradze.github.io/Second-Brain/en/) .
  Next was moving that to git for living, so I wont have to modify and tweak master branch manually or even build over and over again for that I have 3 different branches `master`, `posts`, `For-Hosting` witch have different proposes.
  - `master` contain whole thing , that also where building site happens.
  - `posts` is mostly clear branch but I might change that to contain all posts but what it does RN is with GitHub action when someone pushes to that branch, it moves every `.md` files to master branch in `content/Posts`, and then gets cleared.
  - `For-Hosting` is what name suggests and it contains `public` folder from `master` witch is already built site
  
  ### How can you use it??
  first I made this because **brain in not for containing ideas but for creating them** and also **knowledge should be shared** and most importantly I kind of want to see what I did  in past and look over **what have I done**. 
1. **Fork GitHub repository**
   - first make GitHub account [here](https://github.com/signup)
   - fork my repository from [here](https://github.com/demetrebadzaradze/Second-Brain/fork) , **uncheck `Copy the master branch only` field**.
   - go over to `actions` tab and enable it.
   - then setup GitHub pages in `settings/pages` tab and change the branch from `None` to `For-Hosting` and click on `save`.
1. **Edit `hugo.toml` file to your liking**
   - first thing to edit is `baseURL="<your url>"`, so it should be your URL in double quotes.
    your websites' URL should be in `settings/pages` tab, `Your site is live at <link>` so paste that link into  `baseURL`.
    mine looks like this: `baseURL = "https://demetrebadzaradze.github.io/Second-Brain/"`
    - in `[params.author]` change `name` and `about` as you would like.
    - you can also change `copyright`, `homeSubtitle`, `footerCopyright`, `giturl` if you want.
    - also change the `[[params.socialLinks]]` as you want.
    you can add some testing posts for changes to be applied and for that go to posts branch and just add .md file and commit.
3. **setup local repo**
   - go to the target directory on your windows machine and open CMD in there and clone your repo
     ```bash
     git clone <your-repo-url.git>
		```
	- and then open that folder as vault and don't replace `.obsidian` folder with new one old one contains plugins and upon opening vault it will you if you trust those plugins witch are [shell commands](https://publish.obsidian.md/shellcommands/Index) for publishing with git (you can do it with `ctrl+p` and the type `publish` and run that command) and also `templer` but no templates. I'm thinking of using core plugin `templates` for this (you can add template with making new folder and putting  template like this in there:
	```md
		---
			title: {{title}}
			description: Enter a description here
			date: {{date}}
			draft: false
			toc: true
			ShowLastmod: true
		---
	```
	and you are all setup.


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
	 - **make something to make this configuration and setup for new users.**
