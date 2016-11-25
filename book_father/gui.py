import easygui
flavor = easygui.choicebox("what is your favorit ice cream flavor?",
                           choices=['vanilla','chocolate','strawberry'])
easygui.msgbox('you picked' + flavor)