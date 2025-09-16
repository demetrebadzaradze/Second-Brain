---
title: About Second-Brain
description: Everything about this site ↓↓↓
draft: false
toc: true
ShowLastmod: false
---

## What is Second Brain

Second brain is a eye opening concept (least for me), Witch underlines the fact that **human brain is for creating ideas not for storing them.** This really makes sence, who knows how many ideas one had but got forgotten in a day. So the solution is to put your newborn ideas somewere accessible, to come back to and that gave born to all of this. 

---

## What is going on here

So this website is served by github pages from [my repository](https://github.com/demetrebadzaradze/Second-brain) and that is setup in such a way that, when local notes get pushed they get pretty and show up on the site, like this page witch was just a note on my phone into this webpage. With [obsidian](https://obsidian.md) integration this is even simpler. 

---

## How It Works

Second Brain leverages a robust technical setup to convert local notes into a live website:
1. Repository Structure:
    - The project is hosted in the Second Brain GitHub repository, which uses three key branches:
      - **Master**: Contains the full project, including Hugo configurations and the build pipeline.
      - **Posts**: A dedicated branch for submitting new Markdown posts, automatically cleared after processing.
      - **For-Hosting**: Hosts the static site (`public` folder) served via GitHub Pages.
1. Workflow:
    - Write a post as a Markdown file in Obsidian or another editor.
    - Use a custom Obsidian command to push the post to the `posts` branch.
    - A GitHub Action triggers on push, moving `.md` files to `master/content/Posts/`.
    - Hugo generates a static site using the **Hermit-v2** theme, configured in `hugo.toml`.
    - The generated `public` folder is copied to the `For-Hosting` branch and published via GitHub Pages.
1. Obsidian Integration:
    - Obsidian’s note-taking environment simplifies content creation.
    - Plugins enable seamless publishing to GitHub, eliminating the need for manual Git commands.
  
---

## Why Second Brain?

Second Brain empowers users to:
- Capture Ideas Effortlessly: Turn notes into published posts with minimal effort.
- Share Knowledge: Make your insights accessible to a global audience.
- Build a Portfolio: Showcase programming projects, tutorials, and reflections in a professional format.
Whether you’re a developer documenting technical projects or a writer sharing insights, Second Brain provides a flexible, open-source platform to bring your ideas to life.

---

## Get Involved

Explore the [GitHub repository](https://github.com/demetrebadzaradze/Second-Brain/) to set up your own **Second Brain** or contribute to the project. Check out the [README](https://github.com/demetrebadzaradze/Second-Brain/blob/master/README.md) for setup instructions and join the community to share your ideas!
