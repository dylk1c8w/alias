import streamlit as st
from random import choice
from string import digits, ascii_letters


def main():
    length = 12
    password = ""
    x = list(digits)
    x.extend(ascii_letters)
    for index in range(length):
        password += choice(x)
    st.title("パスワード生成")
    st.write(password)

    # if "red_flag" not in st.session_state:
    #     st.session_state.red_flag = read(file_path="red.cfg")
    # if "blue_flag" not in st.session_state:
    #     st.session_state.blue_flag = read(file_path="blue.cfg")
    # st.session_state.red_flag = read(file_path="red.cfg")
    # st.session_state.blue_flag = read(file_path="blue.cfg")
    # print("0", st.session_state.red_flag, st.session_state.blue_flag)

    # if (st.session_state.red_flag == "0") and (st.session_state.blue_flag == "0"):
    #     st.title("誕生日おめでとう!")
    #     st.write("赤い封筒と青い封筒のどっちか選んで!")

    #     red_image = Image.open('red.png')
    #     st.image(red_image, use_column_width=True)
    #     red_btn = st.button('赤い封筒にする')
    #     if red_btn:
    #         st.session_state.red_flag = "1"
    #         write(file_path="red.cfg", content="1")
    #         st_autorefresh(interval=100, limit=100)

    #     blue_image = Image.open('blue.png')
    #     st.image(blue_image, use_column_width=True)
    #     blue_btn = st.button('青い封筒にする')
    #     if blue_btn:
    #         st.session_state.blue_flag = "1"
    #         write(file_path="blue.cfg", content="1")
    #         st_autorefresh(interval=100, limit=100)
        
    #     print("1", st.session_state.red_flag, st.session_state.blue_flag)
    # else:
    #     st.title("当たり!")
    #     st.write("↓景品のAmazonギフト券↓")
    #     st.write("xxxxxxxxxx")


if __name__ == "__main__":
    main()
