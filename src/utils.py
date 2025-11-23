def render_user_content(user_content):
    html = f"<div>{user_content}</div>"
    return html

def execute_system_command(user_input):
    import os
    command = f"ls -la {user_input}"
    os.system(command)
