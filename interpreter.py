def interpreter(input, output):
    i = open(input, 'r')
    o = open(output, 'w')

    array = list();
    stack = list(); #this stack contains elements in backwards order as i am appending, so pop it into output file
    bindings = [("","")];
    # functions = list(list()) ;
    functions = [[] for _ in range(50)]
    foo=0;
    flag = True
    for line in i:
        array.append(line);

    # i=-1 #pointer to current array element

    for a in array:
        # i++
        word = str(a[0])+str(a[1])+str(a[2])

        if(word == "pus" and flag):
            i=5; val="";
            while (str(a[i])!="\n" and i<len(str(a))) : #checking for backslash-n instead of just backslash
                val = val + str(a[i])
                i=i+1

            if(ord(val[0])<58 and ord(val[0])>47 ):  #case of positive Int
                if(val.isdigit()):     #note: isdigit works only on string and "-32" gives false
                    stack.append(int(val))
                else:
                    stack.append(":error:")
            elif(ord(val[0])==45):  #case of negative int
                val = val[1:(len(val))]
                if(val.isdigit() and int(val)!=0): # consider -x; pop sign while checking
                    val= "-"+val
                    stack.append(int(val))
                elif(val.isdigit() and int(val)==0): #case of -0, pop sign while placing;
                    stack.append(int(val))
                else:
                    stack.append(":error:")
            elif(ord(val[0])==34):    #case of String (with a quotation mark opening-closing)
                val = val[1:(len(val)-1)]        #quotation symbols remove
                val =  "_"+ val                                # extra symbol to diff names and strings
                stack.append(str(val))
            elif((ord(val[0])<91 and ord(val[0])>64) or (ord(val[0])<123 and ord(val[0])>96)): #case of Name (begins with letter)
                stack.append(str(val))  #details to be added later

            elif(ord(val[0])==58):
                if(ord(val[1])==84 or ord(val[1])==116):
                    stack.append(":true:")
                elif(ord(val[1])==70 or ord(val[1])==102):
                    stack.append(":false:")
                else:
                    stack.append(":error:")

        elif(word == "neg" and flag):
            # print('here')
            if(len(stack)==0):
                stack.append(":error:")
            else:
                pop1 = stack.pop()
                popop = pop1
                p=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                if(pop1==bindings[p][0]):
                    pop1 = bindings[p][1]
                if(isinstance((pop1), int)):
                    stack.append(int(pop1)*(-1))
                else:
                    stack.append(popop)
                    stack.append(":error:")
        elif(word == "pop" and flag):
            if(len(stack)==0):
                stack.append(":error:")
            else:
                stack.pop()
        elif(word== "add" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                popop = pop1
                copop = pop2
                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                if(pop1==bindings[p][0]):
                    pop1 = bindings[p][1]
                if(pop2==bindings[q][0]):
                    pop2 = bindings[q][1]

                if(isinstance((pop1), int) and isinstance((pop2), int)):
                    stack.append(int(pop2)+int(pop1))
                else:
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
        elif(word== "sub" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                popop = pop1
                copop = pop2
                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                if(pop1==bindings[p][0]):
                    pop1 = bindings[p][1]
                if(pop2==bindings[q][0]):
                    pop2 = bindings[q][1]
                if(isinstance(pop1, int) and isinstance(pop2, int)):
                    stack.append(int(pop2)-int(pop1))
                else:
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
        elif(word== "mul" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                copop = pop2
                popop = pop1
                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;

                if(len(bindings)>1 and pop1==bindings[p][0]):
                    pop1 = bindings[p][1]

                if(pop2==bindings[q][0]):
                    pop2 = bindings[q][1]

                if(isinstance(pop1, int) and isinstance(pop2, int)):
                    stack.append(int(pop1)*int(pop2))
                else:
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
        elif(word== "div" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                # print("here")
                pop1 = stack.pop()
                pop2 = stack.pop()
                copop = pop2
                popop = pop1
                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0]):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                if(pop1==bindings[p][0]):
                    pop1 = bindings[p][1]
                if(pop2==bindings[q][0]):
                    pop2 = bindings[q][1]
                if(pop1==0):
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
                elif(isinstance(pop1, int) and isinstance(pop2, int)):
                    stack.append(int(pop2)//int(pop1))
                else:
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
        elif(word== "rem" and flag):
            if(len(stack)<=1):
                stack.append(":error:")
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                copop = pop2
                popop = pop1
                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                if(pop1==bindings[p][0]):
                    pop1 = bindings[p][1]
                if(pop2==bindings[q][0]):
                    pop2 = bindings[q][1]
                if(pop1==0):
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
                elif(isinstance(pop1, int) and isinstance(pop2, int)):
                    stack.append(int(pop2)%int(pop1))
                else:
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
        elif(word=="swa" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                stack.append(pop1)
                stack.append(pop2)

        elif(word=="qui" and flag):
            p=0
            while(p<(len(stack))):
                if((str(stack[p])[0])=="_"):
                    stack[p] = stack[p][1:(len(stack[p]))]
                p=p+1
            break

        elif(word=="cat" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                pop1 = str(stack.pop())
                pop2 = str(stack.pop())
                popop = pop1
                copop = pop2

                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                if(pop1==bindings[p][0]):
                    pop1 = bindings[p][1]
                if(pop2==bindings[q][0]):
                    pop2 = bindings[q][1]

                if(str(pop1[0])!="_" or str(pop2[0])!="_"):
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
                else:
                    pop1 = pop1[1:(len(pop1))]
                    pop2 = pop2[1:(len(pop2))]
                    stack.append("_" + pop2 + pop1)
        elif(word=="and" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                pop1 = str(stack.pop())
                pop2 = str(stack.pop())
                popop = pop1
                copop = pop2

                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                if(pop1==bindings[p][0]):
                    pop1 = (":" + bindings[p][1]+ ":")
                if(pop2==bindings[q][0]):
                    pop2 = (":" + bindings[q][1]+ ":")


                if((pop1!=":true:" and pop1!=":false:") or (pop2!=":true:" and pop2!=":false:")):
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
                else:

                    if(pop1==":true:" or pop1==":false:"):
                        pop1 = pop1[1:(len(pop1)-1)]
                    if(pop2==":true:" or pop2==":false:"):
                        pop2 = pop2[1:(len(pop2)-1)]
                    if(str(pop1[0]) == "t" and str(pop2[0])=="t"):
                        stack.append(":true:")
                    else:
                        stack.append(":false:")
        elif(word=="or\n" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
                # print("here")
            else:
                pop1 = str(stack.pop())
                pop2 = str(stack.pop())
                popop = pop1
                copop = pop2

                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                if(pop1==bindings[p][0]):
                    pop1 = (":" + bindings[p][1]+ ":")
                if(pop2==bindings[q][0]):
                    pop2 = (":" + bindings[q][1]+ ":")


                if((pop1!=":true:" and pop1!=":false:") or (pop2!=":true:" and pop2!=":false:")):
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
                    # print("here")
                else:
                    if(pop1==":true:" or pop1==":false:"):
                        pop1 = pop1[1:(len(pop1)-1)]
                    if(pop2==":true:" or pop2==":false:"):
                        pop2 = pop2[1:(len(pop2)-1)]
                    if(str(pop1[0]) == "t" or str(pop2[0])=="t"):
                        stack.append(":true:")
                    else:
                        stack.append(":false:")
        elif(word=="not" and flag):
            if(len(stack)==0 ):
                stack.append(":error:")
            else:
                pop1 = str(stack.pop())
                popop = pop1

                p=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                if(pop1==bindings[p][0]):
                    pop1 = (":" + bindings[p][1]+ ":")


                if(pop1!=":true:" and pop1!=":false:"):
                    stack.append(popop)
                    stack.append(":error:")
                else:
                    if(pop1==":true:" or pop1==":false:"):
                        pop1 = pop1[1:(len(pop1)-1)]
                    if(str(pop1[0]) == "t"):
                        stack.append(":false:")
                    else:
                        stack.append(":true:")
        elif(word=="equ" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                popop = pop1
                copop = pop2

                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                if(pop1==bindings[p][0]):
                    pop1 = (bindings[p][1])
                if(pop2==bindings[q][0]):
                    pop2 = (bindings[q][1])

                if(isinstance(pop1, int) and isinstance(pop2, int)):
                    if(str(pop1) == str(pop2)):
                        stack.append(":true:")
                    else:
                        stack.append(":false:")
                else:
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
        elif(word=="les" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                popop = pop1
                copop = pop2

                p=(len(bindings)-1);
                q=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                if(pop1==bindings[p][0]):
                    pop1 = (bindings[p][1])
                if(pop2==bindings[q][0]):
                    pop2 = (bindings[q][1])

                if(isinstance(pop1, int) and isinstance(pop2, int)):
                    if(pop2 < pop1):
                        stack.append(":true:")
                    else:
                        stack.append(":false:")
                else:
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
        elif(word=="if\n" and flag):
            if(len(stack)<3):
                stack.append(":error:")
            else:
                pop1 = stack.pop()
                pop2 = stack.pop()
                pop3 = stack.pop()
                popop = pop1
                copop = pop2
                lopop = pop3
                if(pop1==":true:"):
                    pop1="true"
                if(pop1==":false:"):
                    pop1="false"
                if(pop2==":true:"):
                    po2="true"
                if(pop2==":false:"):
                    pop2="false"
                if(pop3==":true:"):
                    pop3="true"
                if(pop3==":false:"):
                    pop3="false"
                p=(len(bindings)-1);
                q=(len(bindings)-1);
                r=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ):
                    p=p-1;
                while(q>=0 and pop2!=bindings[q][0] ):
                    q=q-1;
                while(r>=0 and pop3!=bindings[r][0]):
                    r=r-1;
                if(pop1==bindings[p][0]):
                    pop1 = (bindings[p][1])
                if(pop2==bindings[q][0]):
                    pop2 = (bindings[q][1])
                if(pop3==bindings[r][0]):
                    pop3 = (bindings[r][1])

                if(pop3[0]!="t" and pop3[0]!="f"):
                    stack.append(lopop)
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
                else:
                    if(pop3[0]=="t"):
                        stack.append(copop)
                    else:
                        stack.append(popop)

        elif(word=="bin" and flag):
            if(len(stack)==0 or len(stack)==1):
                stack.append(":error:")
            else:
                pop1 = stack.pop()   #9 #a  value
                pop2 = stack.pop()   #a #b  name


                popop = pop1
                copop = pop2

                p=(len(bindings)-1);
                while(p>=0 and pop1!=bindings[p][0] ): # if value is any name,name's value is fetched
                    p=p-1;
                if(pop1==bindings[p][0]):
                    pop1 = bindings[p][1]

                q=(len(bindings)-1);
                while(q>=0 and pop2!=bindings[q][0] and bindings[q][0]!="let" ):  #updating value if NAME REPEATS
                    q=q-1;

                if(copop[0]=="_"):
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
                elif(isinstance(pop1, int)):               #int
                    stack.append(":unit:")
                    bindings.append((pop2,pop1))
                elif(pop1[0]=="_"):                      #string
                    # pop1 = pop1[1:(len(pop1))]
                    stack.append(":unit:")
                    bindings.append((pop2 ,pop1))
                elif(pop1==":true:" or pop1==":false:" or pop1==":unit:"):
                    pop1 = pop1[1:(len(pop1)-1)]          #bool
                    stack.append(":unit:")
                    bindings.append((pop2,pop1))
                elif(len(bindings)>1 and pop2==bindings[q][0]):
                    # if(str(pop1)[0]=="_"):                      #string underscore removal
                    #     pop1 = pop1[1:(len(pop1))]
                    # bindings[q]= ((pop2,pop1))
                    bindings.append((pop2,pop1))
                    stack.append(":unit:")
                else:
                    stack.append(copop)
                    stack.append(popop)
                    stack.append(":error:")
        elif(word=="let" and flag):
            stack.append("let")
            bindings.append(("let","let"))
        elif(word=="end" and flag):
            retval= stack.pop()
            final= stack.pop()
            while(final!='let'):
                final = stack.pop()
            z=0
            while(bindings.pop()!=("let","let")):
                z+=1
            stack.append(retval)


        elif(word=="fun" and str(a[3])!="E"):   #funStart
            funname = a[4:(len(a))]
            potato = "fun "+funname
            # stack.append(potato)
            functions[foo].append(potato)
            flag = False   #to prevent normal interpretation
            foo= foo+1


        elif(word=="fun" and str(a[3])=="E"):  #funEnd
            flag=True
            foo=foo+1 #foo refers to latest functions[] which we have
            # stack.append("funEnd")
            stack.append(":unit:")

        elif(flag==False):
            functions[foo].append(a)

        elif(word=="cal"):
            if(len(stack)<2):
                stack.append(":error:")
            else:
                arg = stack.pop()
                nam = stack.pop()

                if((isinstance(arg, int) == False) and arg[0]==":" and arg[1]=="e"):
                    stack.append(arg)
                    stack.append(nam)
                    stack.append(":error")
                else:
                    if((isinstance(arg, int) == False) and arg[0]!=":" and arg[0]!="_"):
                        p=(len(bindings)-1);
                        while(p>=0 and arg!=bindings[p][0]):
                            p=p-1;
                        if(arg==bindings[p][0]):
                            arg = (bindings[p][1])
                    # ||||
                    # use arg after fetching data from list of functions-list
                    bar= foo
                    print("here")
                    while(bar>=0 and len(functions[bar])>0 and functions[bar][0]!=("fun "+name)):
                        print("here0")
                        bar=bar-1
                        if(functions[bar][0]==("fun "+name)):
                            print("here")
                            for fa in functions[bar]:

                                fword = str(fa[0])+str(fa[1])+str(fa[2])

                                if(word == "pus"):

                                    fi=5; fval="";
                                    print("here2")
                                    while (str(fa[fi])!="\n" and fi<len(str(fa))) : #checking for backslash-n instead of just backslash
                                        fval = fval + str(fa[fi])
                                        fi=fi+1

                                    if(ord(fval[0])<58 and ord(fval[0])>47 ):  #case of positive Int
                                        if(val.isdigit()):     #note: isdigit works only on string and "-32" gives false
                                            stack.append(int(fval))
                                        else:
                                            stack.append(":error:")
                                    elif(ord(fval[0])==45):  #case of negative int
                                        fval = fval[1:(len(fval))]
                                        if(fval.isdigit() and int(fval)!=0): # consider -x; pop sign while checking
                                            fval= "-"+fval
                                            stack.append(int(fval))
                                        elif(fval.isdigit() and int(fval)==0): #case of -0, pop sign while placing;
                                            stack.append(int(fval))
                                        else:
                                            stack.append(":error:")
                                    elif(ord(fval[0])==34):    #case of String (with a quotation mark opening-closing)
                                        fval = fval[1:(len(fval)-1)]        #quotation symbols remove
                                        fval =  "_"+ fval                                # extra symbol to diff names and strings
                                        stack.append(str(fval))
                                    elif((ord(fval[0])<91 and ord(fval[0])>64) or (ord(fval[0])<123 and ord(fval[0])>96)): #case of Name (begins with letter)
                                        stack.append(str(fval))  #details to be added later

                                    elif(ord(fval[0])==58):
                                        if(ord(fval[1])==84 or ord(fval[1])==116):
                                            stack.append(":true:")
                                        elif(ord(fval[1])==70 or ord(fval[1])==102):
                                            stack.append(":false:")
                                        else:
                                            stack.append(":error:")

                                elif(fword == "neg"):
                                    # print('here')
                                    if(len(stack)==0):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()
                                        popop = pop1
                                        p=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0]):
                                            p=p-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = bindings[p][1]
                                        if(isinstance((pop1), int)):
                                            stack.append(int(pop1)*(-1))
                                        else:
                                            stack.append(popop)
                                            stack.append(":error:")
                                elif(fword == "pop"):
                                    if(len(stack)==0):
                                        stack.append(":error:")
                                    else:
                                        stack.pop()
                                elif(fword== "add" ):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()
                                        pop2 = stack.pop()
                                        popop = pop1
                                        copop = pop2
                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = bindings[p][1]
                                        if(pop2==bindings[q][0]):
                                            pop2 = bindings[q][1]

                                        if(isinstance((pop1), int) and isinstance((pop2), int)):
                                            stack.append(int(pop2)+int(pop1))
                                        else:
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                elif(fword== "sub"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()
                                        pop2 = stack.pop()
                                        popop = pop1
                                        copop = pop2
                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = bindings[p][1]
                                        if(pop2==bindings[q][0]):
                                            pop2 = bindings[q][1]
                                        if(isinstance(pop1, int) and isinstance(pop2, int)):
                                            stack.append(int(pop2)-int(pop1))
                                        else:
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                elif(fword== "mul"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()
                                        pop2 = stack.pop()
                                        copop = pop2
                                        popop = pop1
                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;

                                        if(len(bindings)>1 and pop1==bindings[p][0]):
                                            pop1 = bindings[p][1]

                                        if(pop2==bindings[q][0]):
                                            pop2 = bindings[q][1]

                                        if(isinstance(pop1, int) and isinstance(pop2, int)):
                                            stack.append(int(pop1)*int(pop2))
                                        else:
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                elif(fword== "div"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        # print("here")
                                        pop1 = stack.pop()
                                        pop2 = stack.pop()
                                        copop = pop2
                                        popop = pop1
                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0]):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = bindings[p][1]
                                        if(pop2==bindings[q][0]):
                                            pop2 = bindings[q][1]
                                        if(pop1==0):
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                        elif(isinstance(pop1, int) and isinstance(pop2, int)):
                                            stack.append(int(pop2)//int(pop1))
                                        else:
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                elif(fword== "rem"):
                                    if(len(stack)<=1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()
                                        pop2 = stack.pop()
                                        copop = pop2
                                        popop = pop1
                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = bindings[p][1]
                                        if(pop2==bindings[q][0]):
                                            pop2 = bindings[q][1]
                                        if(pop1==0):
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                        elif(isinstance(pop1, int) and isinstance(pop2, int)):
                                            stack.append(int(pop2)%int(pop1))
                                        else:
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                elif(fword=="swa"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()
                                        pop2 = stack.pop()
                                        stack.append(pop1)
                                        stack.append(pop2)

                                elif(fword=="qui"):
                                    p=0
                                    while(p<(len(stack))):
                                        if((str(stack[p])[0])=="_"):
                                            stack[p] = stack[p][1:(len(stack[p]))]
                                        p=p+1
                                    break

                                elif(fword=="cat"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = str(stack.pop())
                                        pop2 = str(stack.pop())
                                        popop = pop1
                                        copop = pop2

                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = bindings[p][1]
                                        if(pop2==bindings[q][0]):
                                            pop2 = bindings[q][1]

                                        if(str(pop1[0])!="_" or str(pop2[0])!="_"):
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                        else:
                                            pop1 = pop1[1:(len(pop1))]
                                            pop2 = pop2[1:(len(pop2))]
                                            stack.append("_" + pop2 + pop1)
                                elif(fword=="and"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = str(stack.pop())
                                        pop2 = str(stack.pop())
                                        popop = pop1
                                        copop = pop2

                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = (":" + bindings[p][1]+ ":")
                                        if(pop2==bindings[q][0]):
                                            pop2 = (":" + bindings[q][1]+ ":")


                                        if((pop1!=":true:" and pop1!=":false:") or (pop2!=":true:" and pop2!=":false:")):
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                        else:

                                            if(pop1==":true:" or pop1==":false:"):
                                                pop1 = pop1[1:(len(pop1)-1)]
                                            if(pop2==":true:" or pop2==":false:"):
                                                pop2 = pop2[1:(len(pop2)-1)]
                                            if(str(pop1[0]) == "t" and str(pop2[0])=="t"):
                                                stack.append(":true:")
                                            else:
                                                stack.append(":false:")
                                elif(fword=="or\n"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                        # print("here")
                                    else:
                                        pop1 = str(stack.pop())
                                        pop2 = str(stack.pop())
                                        popop = pop1
                                        copop = pop2

                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = (":" + bindings[p][1]+ ":")
                                        if(pop2==bindings[q][0]):
                                            pop2 = (":" + bindings[q][1]+ ":")


                                        if((pop1!=":true:" and pop1!=":false:") or (pop2!=":true:" and pop2!=":false:")):
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                            # print("here")
                                        else:
                                            if(pop1==":true:" or pop1==":false:"):
                                                pop1 = pop1[1:(len(pop1)-1)]
                                            if(pop2==":true:" or pop2==":false:"):
                                                pop2 = pop2[1:(len(pop2)-1)]
                                            if(str(pop1[0]) == "t" or str(pop2[0])=="t"):
                                                stack.append(":true:")
                                            else:
                                                stack.append(":false:")
                                elif(fword=="not"):
                                    if(len(stack)==0 ):
                                        stack.append(":error:")
                                    else:
                                        pop1 = str(stack.pop())
                                        popop = pop1

                                        p=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = (":" + bindings[p][1]+ ":")


                                        if(pop1!=":true:" and pop1!=":false:"):
                                            stack.append(popop)
                                            stack.append(":error:")
                                        else:
                                            if(pop1==":true:" or pop1==":false:"):
                                                pop1 = pop1[1:(len(pop1)-1)]
                                            if(str(pop1[0]) == "t"):
                                                stack.append(":false:")
                                            else:
                                                stack.append(":true:")
                                elif(fword=="equ"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()
                                        pop2 = stack.pop()
                                        popop = pop1
                                        copop = pop2

                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = (bindings[p][1])
                                        if(pop2==bindings[q][0]):
                                            pop2 = (bindings[q][1])

                                        if(isinstance(pop1, int) and isinstance(pop2, int)):
                                            if(str(pop1) == str(pop2)):
                                                stack.append(":true:")
                                            else:
                                                stack.append(":false:")
                                        else:
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                elif(fword=="les"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()
                                        pop2 = stack.pop()
                                        popop = pop1
                                        copop = pop2

                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = (bindings[p][1])
                                        if(pop2==bindings[q][0]):
                                            pop2 = (bindings[q][1])

                                        if(isinstance(pop1, int) and isinstance(pop2, int)):
                                            if(pop2 < pop1):
                                                stack.append(":true:")
                                            else:
                                                stack.append(":false:")
                                        else:
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                elif(fword=="if\n"):
                                    if(len(stack)<3):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()
                                        pop2 = stack.pop()
                                        pop3 = stack.pop()
                                        popop = pop1
                                        copop = pop2
                                        lopop = pop3
                                        if(pop1==":true:"):
                                            pop1="true"
                                        if(pop1==":false:"):
                                            pop1="false"
                                        if(pop2==":true:"):
                                            po2="true"
                                        if(pop2==":false:"):
                                            pop2="false"
                                        if(pop3==":true:"):
                                            pop3="true"
                                        if(pop3==":false:"):
                                            pop3="false"
                                        p=(len(bindings)-1);
                                        q=(len(bindings)-1);
                                        r=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ):
                                            p=p-1;
                                        while(q>=0 and pop2!=bindings[q][0] ):
                                            q=q-1;
                                        while(r>=0 and pop3!=bindings[r][0]):
                                            r=r-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = (bindings[p][1])
                                        if(pop2==bindings[q][0]):
                                            pop2 = (bindings[q][1])
                                        if(pop3==bindings[r][0]):
                                            pop3 = (bindings[r][1])

                                        if(pop3[0]!="t" and pop3[0]!="f"):
                                            stack.append(lopop)
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                        else:
                                            if(pop3[0]=="t"):
                                                stack.append(copop)
                                            else:
                                                stack.append(popop)

                                elif(fword=="bin"):
                                    if(len(stack)==0 or len(stack)==1):
                                        stack.append(":error:")
                                    else:
                                        pop1 = stack.pop()   #9 #a  value
                                        pop2 = stack.pop()   #a #b  name

                                        popop = pop1
                                        copop = pop2

                                        p=(len(bindings)-1);
                                        while(p>=0 and pop1!=bindings[p][0] ): # if value is any name,name's value is fetched
                                            p=p-1;
                                        if(pop1==bindings[p][0]):
                                            pop1 = bindings[p][1]

                                        q=(len(bindings)-1);
                                        while(q>=0 and pop2!=bindings[q][0] and bindings[q][0]!="let" ):  #updating value if NAME REPEATS
                                            q=q-1;

                                        if(copop[0]=="_"):
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                        elif(isinstance(pop1, int)):               #int
                                            stack.append(":unit:")
                                            bindings.append((pop2,pop1))
                                        elif(pop1[0]=="_"):                      #string
                                            # pop1 = pop1[1:(len(pop1))]
                                            stack.append(":unit:")
                                            bindings.append((pop2 ,pop1))
                                        elif(pop1==":true:" or pop1==":false:" or pop1==":unit:"):
                                            pop1 = pop1[1:(len(pop1)-1)]          #bool
                                            stack.append(":unit:")
                                            bindings.append((pop2,pop1))
                                        elif(len(bindings)>1 and pop2==bindings[q][0]):
                                            # if(str(pop1)[0]=="_"):                      #string underscore removal
                                            #     pop1 = pop1[1:(len(pop1))]
                                            # bindings[q]= ((pop2,pop1))
                                            bindings.append((pop2,pop1))
                                            stack.append(":unit:")
                                        else:
                                            stack.append(copop)
                                            stack.append(popop)
                                            stack.append(":error:")
                                elif(fword=="let"):
                                    stack.append("let")
                                    bindings.append(("let","let"))
                                elif(fword=="end"):
                                    fretval= stack.pop()
                                    ffinal= stack.pop()
                                    while(ffinal!='let'):
                                        ffinal = stack.pop()
                                    z=0
                                    while(bindings.pop()!=("let","let")):
                                        z=z+1
                                    stack.append(fretval)




        # print("array:")
        # print(array)
        # print("bindings:")
        # print(bindings)
        # print("\t")
        print("stack:")
        print(stack)
        print("functions:")
        print(functions)


    while(len(stack)!=0):
        p=stack.pop()
        o.write(str(p)+'\n')


interpreter('input.txt', 'output.txt')
