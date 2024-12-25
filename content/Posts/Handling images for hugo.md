---
title: Handling images for hugo
date: 2024-12-22
description : "how i handle images for docker"
toc : true
ShowLastmod : true
---
# Plan
so what Hugo want's is to have all images that its gonna use in `static/images` also link needs to be appropriate.
so for something this simple and easy I wrote a ==python script== that:
- reads all `.md` files in a directory 
- finds all images in those files 
- copies images to `static/image` files 
- copes `.md` files into `content/posts`

here is script :
```python
import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"D:\USER\Notes\Important\BlogPosts"
images_dir = r"D:\USER\Notes\Important"
static_images_dir = r"D:\USER\Projects\SecondBrain\static\images"
md_output_dir = r"D:\USER\Projects\SecondBrain\content\Posts"


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
            new_image_path = f"Second-Brain/images/{image_new_filename}"

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

print("\nProcessing complete!")
```


# Types of image syntax in markdown file
in `.md` file there is many ways to insert image here is some:
1. `![Alt text](image_url)`
	this is simple when you copy file that online and after pasting it this is how its formatted. `image_url`  represents online URL of image like:  https://m.media-amazon.com/images/I/61oJQApbXkL._AC_SL1002_.jpg.
	and `Alt text` is just a label
1. `![Alt text](path/to/image.jpg)`
	now this is local and its a full path
3. `![Alt text](path/to/image%20with%20spaces.jpg)`
	this is also local but with spaces this is actually tricky one, because you cant actually have spaces in URI  so they are replaced with `%20`.
5. 
	```
	![A PNG Image](image.png) 
	![A JPEG Image](image.jpg) 
	![An SVG Logo](logo.svg)
	```
	this is also local and this also means that it's in same directory
1. `![[image.png]]` 
	this doesn't one is same as 4 but it doesn't has label

