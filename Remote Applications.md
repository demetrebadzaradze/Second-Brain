---
title: Remote Applications
description: Dockerized applications can run remotely and feel native on your system. By combining them with simple aliases, you can make these tools behave like local apps while actually being powered from the cloud.
date: 2025-09-16
draft: false
toc: true
ShowLastmod: true
---

## What Are Remote Apps?

In the traditional software world, installing an application meant dealing with dependencies, OS differences, or compatibility issues. But modern computing gives us a better option: **remote applications**.  

By "remote," I mean apps that are not tied to your local machine but instead run through **Docker containers**. With Docker, you no longer care whether you’re on Ubuntu, Fedora, macOS, or even Windows—if Docker runs there, the app runs there.  

The difference is: instead of thinking of them as "local installs," you start treating them as **on-demand tools** that live in the cloud or on a server.

This approach unlocks **portability**, **reliability**, and **ease of use** across environments.

---

## A Practical Example: Oxker

Take [Oxker](https://github.com/mrjackwills/oxker), a simple TUI that displays Docker containers on your machine. To run it, they provide a one-liner:

```bash
docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock:ro --pull=always mrjackwills/oxker
```
This is great—it spins up Oxker instantly, always with the latest version. But typing this every time? Not very friendly.

Instead, imagine simply running:
```bash
oxker
```
That feels like a **native application**, even though it’s actually a **remote container**. Smooth, minimal, and intuitive.

--- 

## The Power of Aliases

This magic happens through something as simple as a Linux [alias](https://phoenixnap.com/kb/linux-alias-command). By creating an alias that maps `oxker` to the full `docker run` command, you get the best of both worlds:

- No installation headaches
- Always up to date (since it pulls the latest container)
- Works anywhere Docker runs
- Feels like a real, local command
- 
This is a small trick, but it changes your workflow dramatically. Suddenly, remote containerized apps behave like first-class citizens on your machine.

---

## How to Set Up Aliases for Remote Apps

Here’s how you can turn any Docker command into a native-feeling app:

1. **Open your shell configuration file** (depending on what you use):
    - For Bash:
```bash
		nano ~/.bashrc
```
    - For Zsh:
```bash
		nano ~/.zshrc
```

2. **Add an alias for your Dockerized app.** For Oxker, paste:
    ```bash
    alias oxker="docker run --rm -it -v /var/run/docker.sock:/var/run/docker.sock:ro --pull=always mrjackwills/oxker"
    ```
    
3. **Apply the changes** without restarting:
	```bash
    source ~/.bashrc 
    # or for Zsh 
    source ~/.zshrc
	```
	
4. **Run it just like a native app:**
    ```bash 
	oxker
    ```

That’s it! You’ve created a remote app experience.

---

## Why This Matters

Think about the implications:

- **Lightweight Device Support**  
    Have a weaker laptop and don't want to download apps No problem. Let a server host the applications, while your device just runs containers from server.
    
- **No More Setup Hell**  
    How many times have you wasted hours setting up dev tools or debugging dependencies? With remote apps, you bypass all of that.
    
- **Collaboration Made Simple**  
    You don’t even need your own server. Publish the container to Docker Hub, and anyone can run the exact same version instantly. Consistency for teams, zero friction for users.
    

This is not just about convenience—it’s a **paradigm shift in how we think about software distribution**.

---

## The Downsides of Remote Apps

As powerful as remote applications are, they do come with trade-offs worth keeping in mind:

- **Performance Overhead**  
  Running apps in Docker and pulling them on-demand is not as fast as having them installed natively. For heavy tools, this can mean longer startup times.  
- **Network Dependency**  
  If your alias depends on pulling images from Docker Hub or another registry, you need a stable internet connection. Offline use is limited unless you cache the images locally.  
- **Storage Usage**  
  Each image still takes up disk space after the first pull. Over time, unused containers and images can clutter your system if you don’t prune them.  
- **Security Considerations**  
  Running third-party containers always carries some risk. You need to trust the publisher or audit the Dockerfile to ensure the container is safe. 
- **Learning Curve**  
  For people new to Docker, the setup can feel unfamiliar compared to a simple `apt install` or `brew install`. While aliases simplify usage, the underlying concepts still require some understanding.  

but I'm sure there is many use cases for this kind of setup.

---

## The Future of Remote Apps

I believe this should be the standard way we think about applications: **remote, containerized, and alias-driven**.

Instead of bloating our systems with installs and configs, we can adopt a lightweight, cloud-first approach:

- Define apps as containers
- Publish them for universal access    
- Alias them into our local workflow

The end result? A system where your local machine feels infinite, powered by remote applications.

---

## Final Thoughts

Remote applications are not just a technical trick—they represent a **new mindset**:

- Apps that run anywhere
- Apps that are always up-to-date
- Apps that feel local, but are powered remotely

If you start adopting this approach in your workflow, you’ll notice how much friction disappears. Suddenly, your environment is cleaner, your setup is faster, and your tools are more reliable.

It’s not just about saving keystrokes. It’s about **building a future where software is portable, accessible, and remote by default.**