class evaluate_postfix:
    def __init__(self):
        self.items=[]
        self.size=-1
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
        self.size+=1
    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.size-=1
            return self.items.pop()
    def seek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.size]
    def evalute(self,expr):
        for i in expr:
            if i in '0123456789':
                self.push(i)
            else:
                op1=self.pop()
                op2=self.pop()
                result=self.cal(op2,op1,i)
                self.push(result)
        return self.pop()
    def cal(self,op2,op1,i):
        if i is '*':
            return int(op2)*int(op1)
        elif i is '/':
            return int(op2)/int(op1)
        elif i is '+':
            return int(op2)+int(op1)
        elif i is '-':
            return int(op2)-int(op1)
s=evaluate_postfix()
expr=input('enter the postfix expression')
value=s.evalute(expr)
print('the result of postfix expression',expr,'is',value)

