import gradio as gr
from app.core.assistant import handle_input
from app.core.chat_mode import handle_chat

def respond(message, mode):
    if not message.strip():
        return ""

    if mode == "chat":
        return handle_chat(message)
    else:
        return handle_input(message)

with gr.Blocks(title="Personal Assistant") as demo:
    gr.Markdown(
        """
        # 🤖 Personal Assistant  
        **Task mode** → commands & memory  
        **Chat mode** → AI conversation
        """
    )

    mode = gr.Radio(
        ["task", "chat"],
        value="task",
        label="Mode"
    )

    chatbot = gr.Chatbot(height=450)
    msg = gr.Textbox(
        placeholder="Type your message...",
        show_label=False
    )

    def user_message(user_msg, history, mode):
        reply = respond(user_msg, mode)
        history.append((user_msg, reply))
        return "", history

    msg.submit(
        user_message,
        [msg, chatbot, mode],
        [msg, chatbot]
    )

demo.launch()
