from tkinter import *

root = Tk()
root.title("17-5")

yscrollbar = Scrollbar(root)
xscrollbar = Scrollbar(root, orient=HORIZONTAL)
text = Text(root, height=5, width=30, wrap="none")
yscrollbar.pack(side=RIGHT, fill=Y)
xscrollbar.pack(side=BOTTOM, fill=X)
text.pack()
yscrollbar.config(command=text.yview)
xscrollbar.config(command=text.xview)
text.config(yscrollcommand=yscrollbar.set)
text.config(xscrollcommand=xscrollbar.set)
str = """asdlk;jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjasdffffffffffffffffffffffffas;dlkf;aldkfj;aklsdjf;laksjdf;lkasj;fl
kajs;dfj;asldk;flkj;alkj;lkj;lkj;lksj;lkjs;lkj;lj;lkjl;kj;klj;lkjert hd;ljlkj;lkj;lkjasdfasdfdsfadf f dsf f dad
;adklfja;lskdj;flkj;lkja;lkjd fhpqourvpoqeiu proiqeru dfh kjwh g ert h hrtdfasasdfasdfasdf adfvadf fgdfg ghhghg
qporiu pqoiuerp ioufnogv o iieury oiuqpofiusnpoaiu podfiupnoiupaoeifu asdfa dfsas g hfsa dfsg hdgjddddndhnfgfgg
epoafi uopaeir fuiuyufrom tkinter import *root = Tk()root.title("17-")qwervnuopiiiiii hjklasdfqervyuiow bdf hjk
ext = Text(root)text.pack()if __name__ == '__main__':mainloop()i yesiwer yt gdrftgvbyukljmo,hrfgbujkmlo,sdthyul
uqvpoierupnoiu pchvbieru  opv upqoiuert h lfkavslikrvuaeprivevawiurdfqvunopfiweqwevunopria klfdfkajdfhfuwoiuyfi
 perio poiu dsopuqpaoiweuf poiawupeofksdfjhlsiepqsgvhbt wergy etyhfdqwercnuiopppppppppklkdhflkjhlkjhjkhlkhadjfh
 qawerg wvpergnuimotvyunoeriumiopqwecrvybsrgnuiofw4tvrvwertrtvweadfsafa dfadvqwervqweertybnet yunritm wretbwert
 jjjjjjjjjjjjjjjjjjjasdfkj;lkj;lksj;lkjs;lkj;ljkjd fhpqourvpoqeiu proi iieury oiuqpofiusnpoaitkinter importbwer
 jjjjjjjjjjjjkj;lkj;lkj;kja;lkjd fhpogv o iieuryfrom tkinterpack()if __neru  opv upqiweuf poiawuyunoeriumiop"""
text.insert(END, str)
if __name__ == '__main__':
    mainloop()
