from html import escape
def render_user_content(user_content):
    html = f"<div>{escape(user_content, quote=True)}</div>"
    return html
 def execute_system_command(user_input):
    import subprocess
    subprocess.run(["ls", "-la", "--", user_input], check=True)
    os.system(command)
