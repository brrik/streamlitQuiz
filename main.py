import streamlit as st

st.title("エンジニアなぞなぞ")
st.text("* 答えは全角ひらがなで書いてね！")

st.markdown("---")

st.title("第1問")
st.image("./q1.jpg")
ans1 = st.text_input("1問目 解答：")
if ans1 == "こまんどぷろんぷと" :
    mk = """# :green[正解！]
そりゃぁ窓がたくさん、だもん。Windowsのコマンドは？ってこと！  
まぁPowerShellもあるけど、有名なのはコマンドプロンプトだよね。"""
    st.markdown(mk)
elif ans1 == "":
    pass
else:
    st.markdown("""# :red[不正解]
もうちょっと考えてみよう""")

st.markdown("---")

st.title("第2問")
st.image("./q2.jpg")
ans2 = st.text_input("2問目 解答：")
if ans2 == "たーみなる" :
    mk = """# :green[正解！]
こんどはりんごだね。当然つぎはMacだよね！  
Macのコマンドラインは「ターミナル」って呼ぶよ。ちなみにLinuxのコマンドも使えるんだ！"""
    st.markdown(mk)
elif ans2 == "":
    pass
else:
    st.markdown("""# :red[不正解]
    もうちょっと考えてみよう""")

st.markdown("---")

st.title("第3問")
st.image("./q3.jpg")
ans3 = st.text_input("3問目 解答：")
if ans3 == "えすけーぷ" :
    mk = """# :green[正解！]
この順番、どこかでみたことあるよね？  
そう、キーボードだ！

ってことは、F1の左、全角半角の上にあるのは、ESC。  
そもそも読み方知ってたかな？"""
    st.markdown(mk)
elif ans3 == "":
    pass
else:
    st.markdown("""# :red[不正解]
    もうちょっと考えてみよう""")

st.markdown("---")

st.title("第4問")
st.image("./q4.jpg")
ans4 = st.text_input("4問目 解答：")
if ans4 == "はっしゅ" :
    mk = """# :green[正解！]
鍵盤の黒鍵にバツが入ってる、つまり「シャープじゃないよ！」ってことだね！  
うしろにうっすらある＃マークで、「シャープじゃない」からハッシュ記号だね！  
ふざけてんのかって？  
めっちゃごめん。"""
    st.markdown(mk)
elif ans4 == "":
    pass
else:
    st.markdown("""# :red[不正解]
    もうちょっと考えてみよう""")

st.markdown("---")

st.title("第5問")
st.image("./q5.jpg")
ans5 = st.text_input("5問目 解答：")
if ans5 == "しんすう" :
    mk = """# :green[正解！]
なんだか法則性のない数字だけど、エンジニアならピンときてほしいね！  
これらはプログラミングをしてたらよく出てくる、2進数、8進数、10進数、16進数の数字だね。"""
    st.markdown(mk)
elif ans5 == "":
    pass
else:
    st.markdown("""# :red[不正解]
もうちょっと考えてみよう""")

st.markdown("---")

st.title("第6問")
code6 = """
no_6_list = []
for i in range("い", "と"):
    no_6_list.append(i)

no_6_answer = no_6_list[1]
"""
st.code(code6)
st.text("ヒント：no_6_listの配列長は6")
ans6 = st.text_input("6問目 解答：")
if ans6 == "ろ" :
    mk = """# :green[正解！]
普通なら、当然Range関数に文字なんか入れられないよね。  
でも配列長が6ってことは、「い」から始まって、7文字目が「と」なわけ。  
なんとなく、いろはにほへと、じゃない？  
まぁ、でも、ごめん。"""
    st.markdown(mk)
elif ans6 == "":
    pass
else:
    st.markdown("""# :red[不正解]
    もうちょっと考えてみよう""")

st.markdown("---")

st.title("第7問")
code7 = """
no_7_list = range("い", "す")
no_7_list_2 = []
while len(no_7_list)>0:
    no_7_list_3 = []
    if len(no_7_list)>=5:
        length = 5
    else:
        length = len(no_7_list)
    for i in range(length):
        no_7_list_3.append(no_7_list[0])
        no_7_list.pop(0)
    no_7_list_2.append(no_7_list_3)

no_7_answer = no_7_list_2[4][4]
"""
st.code(code7)
ans7 = st.text_input("7問目 解答：")
if ans7 == "ゐ" or ans7 == "い":
    mk = """# :green[正解！]
またいろは歌ってことはわかったよね？  
で、こんどはちょっと複雑な処理だったね。  
いろは歌を5文字ずつにわけて、リストを多重構造にしたんだね。  
結果、大きい方のリストの4番目、['な', 'ら', 'む', 'う', 'ゐ']のさらに4番目だから、  
「ゐ」だね！  
今回は旧字体も新字体(普通の「い」)も正解だったよ！"""
    st.markdown(mk)
elif ans7 == "":
    pass
else:
    st.markdown("""# :red[不正解]
    もうちょっと考えてみよう""")


st.markdown("---")


st.title("第8問")
st.code("no_8_answer = reverse(||)")
st.write("ヒント：Pythonだと使われない記号だね。JavaScriptとかで調べるといいかも。")
ans8 = st.text_input("8問目 解答：")
if ans8 == "ろ" or ans8 == "RO" or ans8 == "ro" :
    mk = """# :green[正解！]
しっかりと他の言語のことまで調べられました！  
Pythonだと「または」を表すのは「or」だけだけど、  
JavaScriptやC,Rubyなんかだと「||」で「or」を表すんだね。  
それの逆転(reverse)だから、「ろ」「ro」「RO」のいずれかが正解になるよ！"""
    st.markdown(mk)
elif ans8 == "":
    pass
else:
    st.markdown("""# :red[不正解]
    もうちょっと考えてみよう""")


st.markdown("---")

st.title("第9問")
code = """
no_9_answer = []
for i in answers:
    no_19_answer.append(answers[i][0]);
"""
st.code(code)
st.markdown("""
|| FFFFFF
""")
ans9 = st.text_input("9問目 解答：")
if ans9 == "しろいろ" :
    mk = """# :green[正解！]
よくわかったね！最後だけ謎解きみたいだったでしょ？

これまでの答えが全部リストに入ってると考えたら、  
リストのインデックス0は「それぞれの答えの1文字目」だもんね！

それともカラーコード(FFFFFF：白)から解いたかな？

OR記号( || )に気付けたら、どっちからでも解けたよね！"""
    st.markdown(mk)
elif ans9 == "":
    pass
else:
    st.markdown("""# :red[不正解]
    もうちょっと考えてみよう""")