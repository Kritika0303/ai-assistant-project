import streamlit as st

# 🔧 Dummy assistant response generator
def generate_dummy_response(prompt, role):
    if role == "Coding Mentor":
        return f"(Simulated Response)\nAs your coding mentor, here's a helpful explanation for: '{prompt}'"
    else:
        return f"(Simulated Response)\nAs your finance advisor, here's a smart answer for: '{prompt}'"

# 🧠 App Title & Role Switch
st.title("💬 AI Mentor Assistant (Simulated)")
role = st.selectbox("Choose your assistant role:", ["Coding Mentor", "Finance Advisor"])

# 💬 Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": f"You are a helpful {role.lower()}."}
    ]

# 📝 User Input
user_input = st.text_input("Ask your question:")

# 🔘 On button click, simulate assistant reply
if st.button("Get Answer") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    assistant_reply = generate_dummy_response(user_input, role)
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})

    st.write("### 💡 Assistant:")
    st.write(assistant_reply)

# 📜 Chat history
if st.checkbox("Show Chat History"):
    for msg in st.session_state.messages[1:]:  # skip system
        speaker = "🧑 You" if msg["role"] == "user" else "🤖 Assistant"
        st.markdown(f"**{speaker}:** {msg['content']}")

# 💾 Save chat
if st.button("Save Chat to File"):
    with open("chat_log.txt", "w", encoding="utf-8") as f:
        for msg in st.session_state.messages:
            f.write(f"{msg['role']}: {msg['content']}\n")
    st.success("✅ Chat saved to chat_log.txt")
    
