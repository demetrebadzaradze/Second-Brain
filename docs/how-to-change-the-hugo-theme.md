# How to Change the Hugo Theme

Second Brain uses the Hermit-v2 theme by default to provide a clean, modern look for your blog. However, you can easily switch to a different Hugo theme to customize the appearance of your site. This guide provides step-by-step instructions to update the theme by modifying the Git submodule and Hugo configuration.

## Prerequisites

- A forked and cloned copy of the Second Brain repository.
- Git installed on your local machine.
- Basic familiarity with Hugo and Git submodules.
- Access to the repository’s `master` branch for configuration changes.

## Steps to Change the Theme

Follow these steps to replace the Hermit-v2 theme with a new Hugo theme:

1. **Select a New Theme**:

   - Browse the Hugo Themes directory to find a theme that suits your needs.
   - Note the theme’s Git repository URL and the recommended branch (usually `main` or `master`). For example, if you choose the Ananke theme, the repository URL is `https://github.com/theNewDynamic/gohugo-theme-ananke`.

2. **Update the Git Submodule**:

   - Open the `.gitmodules` file in the root of your repository.
   - Replace the existing submodule configuration with the new theme’s details. The file should follow this format:

     ```ini
     [submodule "themes/<theme-name>"]
         path = themes/<theme-name>
         url = <theme-git-repo-url>
         branch = <theme-branch>
     ```

     Example for the Ananke theme:

     ```ini
     [submodule "themes/gohugo-theme-ananke"]
         path = themes/gohugo-theme-ananke
         url = https://github.com/theNewDynamic/gohugo-theme-ananke
         branch = main
     ```
   - Save and commit the updated `.gitmodules` file:

     ```bash
     git add .gitmodules
     git commit -m "Update .gitmodules to use new theme"
     ```

3. **Sync and Update the Submodule**:

   - Remove the existing theme’s submodule data:

     ```bash
     git rm -r themes/hermit-v2
     ```
   - Add and initialize the new theme’s submodule:

     ```bash
     git submodule add --force <theme-git-repo-url> themes/<theme-name>
     ```

     Example:

     ```bash
     git submodule add --force https://github.com/theNewDynamic/gohugo-theme-ananke themes/gohugo-theme-ananke
     ```
   - Ensure the submodule is initialized and updated:

     ```bash
     git submodule update --init --recursive
     ```
   - Commit the changes:

     ```bash
     git add themes/<theme-name>
     git commit -m "Add new theme submodule"
     ```

4. **Update Hugo Configuration**:

   - Open the `hugo.toml` file in the root of your repository.
   - Update the `theme` parameter to match the new theme’s directory name:

     ```toml
     theme = "<theme-name>"
     ```

     Example for Ananke:

     ```toml
     theme = "gohugo-theme-ananke"
     ```
   - Review the theme’s documentation (usually in its `README.md`) for additional configuration options, such as custom parameters or assets. Update `hugo.toml` accordingly.
   - Example for Ananke:

     ```toml
     [params]
       favicon = "images/favicon.ico"
       site_logo = "images/logo.png"
       background_image = "/images/background.jpg"
     ```
   - Save and commit the changes:

     ```bash
     git add hugo.toml
     git commit -m "Update hugo.toml for new theme"
     ```

5. **Test the Theme Locally**:

   - Run the Hugo development server to preview the site with the new theme:

     ```bash
     hugo server
     ```
   - Open `http://localhost:1313` in your browser to verify the theme is applied correctly.
   - Check for errors or missing assets, and consult the theme’s documentation for troubleshooting.

6. **Push Changes to GitHub**:

   - Push the updated `master` branch to your repository:

     ```bash
     git push origin master
     ```
   - The GitHub Action will trigger, rebuilding the site and deploying it to the `For-Hosting` branch for GitHub Pages.

7. **Verify the Live Site**:

   - Visit your site (e.g., `https://<username>.github.io/Second-Brain/`) to ensure the new theme is live.
   - Test navigation, responsiveness, and content rendering on multiple devices.

## Troubleshooting

- **Submodule Errors**: If the submodule doesn’t load, run `git submodule sync` followed by `git submodule update --init --recursive`.
- **Theme Configuration**: Ensure all required parameters are set in `hugo.toml`. Check the theme’s documentation for mandatory settings.
- **Broken Styles**: If the site looks incorrect, verify that theme assets (e.g., CSS, images) are correctly placed in `themes/<theme-name>` or `static/`.
- **GitHub Actions Failure**: Check the Actions tab in your repository for build errors, such as missing dependencies or incorrect paths.

## Additional Tips

- **Backup Your Repository**: Before making changes, create a backup branch (`git branch backup`) to preserve your current setup.
- **Test Theme Compatibility**: Some themes may require specific Hugo versions. Check your Hugo version (`hugo version`) and the theme’s requirements.
- **Customize the Theme**: After switching, customize the theme’s colors, fonts, or layout in `hugo.toml` or by adding custom CSS in `static/css/`.
- **Document Changes**: Update your README or a changelog to note the new theme and any specific configuration steps.

## Need Help?

If you encounter issues or need assistance selecting a theme, check the Hugo Themes directory or open an issue in the Second Brain repository. Contributions to improve theme support are welcome!

---

**License**: The code for Second Brain, including theme configurations, is licensed under the MIT License. Blog content is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. See `content/Posts/LICENSE.md` for details.
