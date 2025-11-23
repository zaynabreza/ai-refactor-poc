import html as html_lib
def render_user_content(user_content):
    html = f"<div>{html_lib.escape(user_content, quote=True)}</div>"
    return html
def execute_system_command(user_input):
    import subprocess
    command = ["ls", "-la", user_input]
    subprocess.run(command, check=True)
    os.system(command)
