import os
import re
import shutil
import subprocess

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"D:\Demetre Badzgaradze\Notes\Important\BlogPosts"
images_dir = r"D:\Demetre Badzgaradze\Notes\Important"
static_images_dir = r"D:\Demetre Badzgaradze\ProgramingProjects\SecondBrain\static\images"
md_output_dir = r"D:\Demetre Badzgaradze\ProgramingProjects\SecondBrain\content\Posts"


# Define the updated image regex pattern to match both image formats:
# 1. ![Alt Text](image-path)
# 2. ![[image-path]]
image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)|!\[\[([^\]]+)\]\]')

def find_and_process_images(md_file):
    print(f"\nProcessing file: {md_file}")
    
    # Read the content of the markdown file
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Find all image references in the Markdown file
    image_references = image_pattern.findall(content)
    print(f"Found {len(image_references)} image references in {md_file}")

    # Process each image reference
    for match in image_references:
        if match[1]:  # Format: ![Alt Text](image-path)
            alt_text = match[0]
            image_path = match[1]
            print(f"Found image (Markdown format): Alt Text: '{alt_text}', Path: {image_path}")
        elif match[2]:  # Format: ![[image-path]]
            alt_text = "image"
            image_path = match[2]
            print(f"Found image (Custom format): Path: {image_path}")

        # If the image path is an online URL, skip it
        if image_path.startswith("http") or image_path.startswith("https"):
            print(f"Skipping online image: {image_path}")
            continue
        
        # Determine if the image is a local file
        image_filename = os.path.basename(image_path)  # Get the file name from the path
        image_extension = os.path.splitext(image_filename)[1].lower()
        print(f"Image file name: {image_filename}, Extension: {image_extension}")

        image_new_filename = image_filename
        image_new_filename = image_new_filename.replace(' ', '_')  # Replace spaces with underscores
        print(f"Updated image filename: {image_new_filename}")

        # Build the full image path in the images directory
        local_image_path = os.path.join(images_dir, image_filename)
        print(f"Checking for image in local folder: {local_image_path}")

        if os.path.exists(local_image_path):
            print(f"Image found in local folder: {local_image_path}")
            
            # The image exists locally, copy it to the Hugo static images directory
            destination_path = os.path.join(static_images_dir, image_new_filename)
            print(f"Copying image to Hugo static images folder: {destination_path}")

            if not os.path.exists(destination_path):  # Only copy if not already copied
                shutil.copy(local_image_path, destination_path)
                print(f"Successfully copied image: {image_filename}")
            else:
                print(f"Image already exists in destination: {destination_path}")

            # Update the image reference in the Markdown file
            new_image_path = f"/images/{image_new_filename}"

            content = content.replace(f"![{alt_text}]({image_path})", f"![{alt_text}]({new_image_path})")
            content = content.replace(f"![[{image_path}]]", f"![{alt_text}]({new_image_path})")
            print(f"Updated image path in Markdown: {new_image_path}")
        else:
            print(f"Image not found in the images folder: {local_image_path}")

    # Save the modified content into the output folder, keeping the original filename
    new_md_file_path = os.path.join(md_output_dir, os.path.basename(md_file))
    print(f"Saving updated Markdown file to: {new_md_file_path}")
    
    with open(new_md_file_path, "w", encoding="utf-8") as file:
        file.write(content)
    
    print(f"Successfully updated and saved Markdown file: {new_md_file_path}")

# Step 2: Process all markdown files in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        md_file_path = os.path.join(posts_dir, filename)
        print(f"\nProcessing Markdown file: {md_file_path}")
        find_and_process_images(md_file_path)

print("\n image and post Processing complete!")

hugo_project_dir = r"D:\Demetre Badzgaradze\ProgramingProjects\SecondBrain"
public_dir = os.path.join(hugo_project_dir, "public")
commit_message = "new post "


# Step 1: Run Hugo to build the site
print("Building the Hugo site...")
try:
    subprocess.run(["hugo"], cwd=hugo_project_dir, check=True)
    print("Hugo site built successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error building Hugo site: {e}")
    exit(1)

# Step 2: Commit and push to the main branch
print("Committing and pushing changes to the main branch...")
try:
    subprocess.run(["git", "add", "."], cwd=hugo_project_dir, check=True)
    subprocess.run(["git", "commit", "-m", commit_message], cwd=hugo_project_dir, check=True)
    subprocess.run(["git", "push", "origin", "master"], cwd=hugo_project_dir, check=True)
    print("Changes pushed to the main branch successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error pushing changes to the main branch: {e}")
    exit(1)

# Step 3: Push the 'public' directory to the hosting branch
print("Pushing 'public' directory to the hosting branch...")
try:
    subprocess.run(
        ["git", "subtree", "push", "--prefix", "public", "origin", "For-Hosting"],
        cwd=hugo_project_dir, check=True
    )
    print("Public directory pushed to the hosting branch successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error pushing 'public' directory: {e}")
    exit(1)