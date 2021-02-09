# http://tinyurl.com/jhrvs94
# 吊された人の絵が完成する前に，単語を当てるゲーム

# hangmanを定義する
def hangman(word):
    wrong = 0 # wrong:間違った回数を記録する
    stages = ["",
             "________        ",
             "|               ",
             "|       |       ",
             "|       o       ",
             "|      /|\      ",
             "|      / \      ",
             "|               "
             ] # stages:間違えるたびに表示される絵の定義
    rletters = list(word) # rletters:hangman関数に渡した引数wordのリストを返す
    board = ["_"] * len(word) # board:wordの文字数だけ"_"を用意する
    win = False 
    print("Welcome to hangman!")

# http://tinyurl.com/ztrp5jc

# 繰り返し処理の部分
    while wrong < len(stages) - 1: # 間違った回数がリスト"stages"の要素を越えない範囲で繰り返す
        print("\n")
        msg = "Gusee the one word." # mag:1文字を入力させるmessage
        char = input(msg) # char:msgに対する入力を読み取る
        if char in rletters: # 答えがに引数wordと一致する文字であれば、、、
            cind = rletters.index(char) # ~~.index(引数)で渡された引数が最初に現れた位置のインデックス値を返す
                                        # cind:wordにおける答えの該当箇所を返す
            board[cind] = char# boardのcind番目を穴埋めする
            rletters[cind] = '$' # 該当箇所が複数ある場合に２個目以降を見つけられるような工夫
        else: # 答えが引数wordに含まれなければ、、、
            wrong += 1
        print(" ".join(board)) # ~~.join(引数)で引数の全ての要素間に~~を追加する
                               # 現在の回答状況を表示する
        e = wrong + 1
        print("\n".join(stages[0:e])) # 絵を表示する
        if "_" not in board: # 全ての文字が穴埋めされたならば、、、
            print("You win!")
            print(" ".join(board))
            win = True
            break

# http://tinyurl.com/zqklqxo

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose.\nThe answer is {}.".format(word))

# http://tinyurl.com/h9q2cpc

hangman("cat") # hangman関数を実行する