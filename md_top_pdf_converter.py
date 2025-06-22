import markdown
import os
from weasyprint import HTML, CSS

def convert_md_to_pdf(markdown_file_path, output_pdf_path, css_file_path =None):
    try:
        with open(markdown_file_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content, extensions=["extra", "codehilite", "sane_lists"])

        final_html = f"""
            
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title> MD to PDF Converter </title>
                    <style>
                        body {{ font-family: sans-serif; line-height: 1.6; margin: 2cm; }}
                        h1, h2, h3, h4, h5, h6 {{ color: #333; }}
                        pre {{ background-color: #f4f4f4; padding: 1em; border-radius: 5px; overflow-x: auto; }}
                        code {{ font-family: monospace; }}
                        table {{ width: 100%; border-collapse: collapse; margin-bottom: 1em; }}
                        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                        th {{ background-color: #f2f2f2; }}
                    </style>
                </head>
                <body>
                    {html_content}
                </body>
            </html>
            """
        
        html = HTML(string=final_html, base_url=os.path.dirname(markdown_file_path))

        stylesheets = []
        if css_file_path and os.path.exists(css_file_path):
            stylesheets.append(CSS(filename=css_file_path))
        
        elif css_file_path:
            print(f"ATTENTION: CSS-File '{css_file_path}' not found.")
        
        html.write_pdf(output_pdf_path, stylesheets=stylesheets)

        print(f"Successfully converted '{markdown_file_path}' to '{output_pdf_path}'.")
    
    except FileNotFoundError:
        print(f"ERROR: The file '{markdown_file_path}' could not be found.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("Conversion process completed.")

