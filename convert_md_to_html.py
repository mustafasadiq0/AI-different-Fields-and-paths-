import markdown
import os

input_dir = '/home/ubuntu/ai_roadmaps_website/src/static'
output_dir = '/home/ubuntu/ai_roadmaps_website/src/templates/roadmaps'

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.md'):
        input_filepath = os.path.join(input_dir, filename)
        output_filename = filename.replace('.md', '.html')
        output_filepath = os.path.join(output_dir, output_filename)

        with open(input_filepath, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        html_content = markdown.markdown(markdown_content)

        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f'Converted {filename} to {output_filename}')


