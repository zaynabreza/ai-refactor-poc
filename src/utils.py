def render_user_content(user_content):
    import html
    html = f"<div>{html.escape(user_content, quote=True)}</div>"
    return html
def execute_system_command(user_input):
    import subprocess
    command = ["ls", "-la", "--", user_input]
    subprocess.run(command, check=True)
    os.system(command)
