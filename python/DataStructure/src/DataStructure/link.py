class linknode():
    def __init__(self,k,n=None):
        self.key=k;
        self.next=n;
def createlist():        #��������
    n=raw_input("enter the num of nodes");
    n=int(n);
    if n<1 :
        return ;
    else :
        a=raw_input("enter the key");
        head=linknode(k=a);

        if n is 1:
            return head;
        else :
            p=head;
            for i in range(1,n):
                a=raw_input("enter a key");
                t=linknode(k=a);
                p.next=t;
                p=t;
            return head;
def printlist(head):    #��ӡ����
    p=head;
    while p!= None:
        print p.key;
        p=p.next;
def listlen(head):��������#����������
    c=0;
    p=head;
    while p!= None:
        c=c+1;
        p=p.next;
    return c;
def insert(head,n):     #����Ԫ��
    if n<1 or n>listlen(head) :
        return ;
    p=head;

    if n is 1:
        a=raw_input("enter a key");
        t=linknode(k=a);
        t.next=head;
        head=t;

    else :
        for i in range(1,n-1):
            p=p.next;
        a=raw_input("enter a key");
        t=linknode(k=a);
        t.next=p.next;
        p.next=t;
    return head;

def dellist(head,n):     #ɾ��
    if n<1 or n>listlen(head):
        return head;
    elif n is 1:
        head=head.next;
    else:
        p=head;
        for i in range(1,n-1):
            p=p.next;
        q=p.next;
        p.next=q.next;
    return head;

def findlist(head,n):   # ����
    p=head;
    if p is None:
        return ;
    while(p!=None):
        if p.key is repr(n):
            print "find it";
            return 1;
        else:
            p=p.next;
    if p is None:
        print "not found";