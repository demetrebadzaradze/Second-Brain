# Second Brain

![Second Brain Logo](/Logo.png)

<p align="center">
  <a href="https://github.com/demetrebadzaradze/Second-Brain/actions">
    <img src="https://github.com/demetrebadzaradze/Second-Brain/actions/workflows/main.yml/badge.svg?branch=posts" />
  </a>
  <a href="https://github.com/demetrebadzaradze/Second-Brain">
    <img src="https://img.shields.io/github/last-commit/demetrebadzaradze/Second-Brain?style=flat-square)" />
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" />
  </a>
  <a href="content/Posts/LICENCE">
    <img src="https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg" />
  </a>
  <a href="https://github.com/demetrebadzaradze/Second-Brain/actions/workflows/pages/pages-build-deployment">
    <img src="https://img.shields.io/badge/GitHub_Pages-222222?style=flat-square&logo=githubpages&logoColor=white" />
  </a>
  <a href="https://gohugo.io/">
    <img src="https://img.shields.io/badge/Hugo-FF4088?style=flat-square&logo=hugo&logoColor=white" />
  </a>
  <a href="https://www.markdownguide.org/">
    <img src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white" />
  </a>
  <a href="https://obsidian.md/">
    <img src="https://img.shields.io/badge/Obsidian-483699?style=flat-square&logo=obsidian&logoColor=white" />
  </a>
</p>

A dynamic **blogging** platform **powered by Hugo, GitHub, and Obsidian** for **seamless content creation and publishing.**

## Table of Contents
- [Overview](#overview)
- [How it works](#how-it-works)
- [Getting Started](#getting-started)
- [Why Use Second Brain?](#why-use-second-brain)
- [Future Plans](#future-plans)
- [Contributing](#contributing)
- [License](#license)

## Overview
Second Brain is a streamlined blogging platform hosted on GitHub, designed for creating and sharing knowledge effortlessly. It leverages Hugo for static site generation, the Hermit-v2 theme for a polished look, and Obsidian for intuitive content creation. Posts are written in Markdown and managed through Git, enabling a frictionless workflow for writers and developers alike.

## How It Works
Second Brain uses a combination of [Hugo](https://gohugo.io/), GitHub, and custom Git branches to manage and deploy content:
- Hugo: Converts Markdown (.md) files into `HTML`, powered by the [Hermit-v2](https://themes.gohugo.io/themes/hermit-v2/), eliminating the need for custom `HTML`, `CSS`, or `JavaScript`.
- GitHub Workflow:
	- `Master` Branch: Contains the entire project, including the Hugo site source and build pipeline.
	- `Posts` Branch: A clean branch for submitting new Markdown posts. A GitHub Action automatically moves posts to the `content/Posts` directory in the master branch and clears the `posts` branch.
	- `For-Hosting` Branch: Hosts the built static site (`public` folder from `master`) for deployment via GitHub Pages.
 - [Obsidian](https://obsidian.md/) Integration: The `posts` branch also includes an `.obsidian` configuration, enabling a custom `publish` command. This allows content to be pushed directly from Obsidian. A Templates folder provides pre-defined front matter for consistent, well-formatted posts.
 
## Getting Started
Follow these steps to set up your own Second Brain blog:
### Prerequisites
- A GitHub account (sign up [here](https://github.com/signup).
- Basic familiarity with Git and Markdown.
- Optional: Obsidian for local note-taking, content creation and predefined configuration, templates and commands.

### Setup Instructions
1. Fork the Repository:
	- Navigate to the Second Brain repository.
	- Fork the repository, ensuring all branches are copied (uncheck "Copy the master branch only").
	- Delete contents of `posts` directory to ensure you my blogs are not on your site. 
	- Enable GitHub Actions in the Actions tab of your forked repository.
1. Configure GitHub Pages:
	- Go to Settings > Pages in your repository.
	- Set the branch to For-Hosting and save. Your site will be live at the URL provided (e.g., https://<username>.github.io/Second-Brain/).
1. Edit Configuration:
	- Open the hugo.toml file in the master branch.
	- Update the baseURL to your GitHub Pages URL (e.g., baseURL = "https://<username>.github.io/Second-Brain/").
	- Customize [params.author] (name and about) and [[params.socialLinks]] as desired.
	- Optionally modify copyright, homeSubtitle, footerCopyright, or giturl. more configuretion option [here](https://gohugo.io/configuration/params/) and [here](https://1bl4z3r.github.io/hermit-V2/en/posts/explaining-configs/) and example `hugo.toml` files [here](https://github.com/1bl4z3r/hermit-V2/blob/main/hugo.toml.example) and [here](https://github.com/1bl4z3r/hermit-V2/blob/staging/hugo.toml) and also [here](https://github.com/demetrebadzaradze/Second-Brain/blob/master/hugo.toml).
1. Add a Test Post:
	- Switch to the posts branch.
	- Create a new .md file with the following front matter:
	```bash
	---
	title: Your Post Title
	description: Enter a description here
	date: 2025-01-15
	draft: false
	toc: true
	ShowLastmod: true
	---
	```
	- Commit and push the file. The GitHub Action will move it to the master branch and trigger a site rebuild.

1. Set Up Locally with Obsidian:
	- Clone your forked repository:
	```bash
 	git clone <your-repo-url.git>
 	```
	- Open the repository in Obsidian.
	- Retain the existing `.obsidian` folder, which includes plugins for publishing (e.g., `shell commands` for Git integration).
 	- to publish a post, use Obsidian’s command palette (`Ctrl+P`), type `publish`, and run the command.
	- Optionally, create templates in a `Templates` folder for consistent post formatting:
	```bash
 	---
	title: {{title}}
	description: Enter a description here
	date: {{date}}
	draft: false
	toc: true
	ShowLastmod: true
	---
    ```

## Why Use Second Brain?
Second Brain is designed to:
- Foster Creativity: Focus on generating ideas rather than storing them, exactly what brain is for.
- Share Knowledge: Make your insights accessible to others.
- Track Progress: Reflect on past work and projects.
It’s ideal for developers, writers, and anyone looking to maintain a portfolio or blog with minimal setup.

## Future Plans
- Portfolio Expansion: Showcase programming projects and technical deep dives.
- Obsidian Integration: Develop a custom Obsidian plugin for seamless post publishing without terminal or web interactions.
- Cross-Platform Support: Extend compatibility beyond Windows to macOS and Linux.
- Simplified Setup: Streamline configuration for non-technical users, reducing setup friction and merge conflicts.
- Content Ideas:
	- Tutorials on home server setups.
	- In-depth guide on Second Brain’s architecture.
	- A roadmap for future projects.

## Contributing
Contributions are welcome! To suggest improvements or report issues:
- Fork the repository.
- Create a new branch for your changes.
- Submit a pull request to the master branch.
leave posts untouched.

## License
- **Code**: The source code, including Hugo configurations, themes, and scripts, is licensed under the [MIT License](LICENSE).
- **Blog Posts**: The content in the `content/Posts` directory is licensed under [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).
