#encoding:utf-8

class JackError(Exception):
    pass

a=1
if a<10:
    raise TabError#抛异常，程序不会往下执行


def adde():
    try:
        a=open("d:\\新建文本文档.txt1","r")
        b=a.read()
        print(b)

    except Exception as msg:
        print("异常: %s" %str(msg))


    except JackError:#使用自己定义的异常
        print(1)
    finally:
        print("最终finally")




if __name__=="__main__":
    a=adde()
