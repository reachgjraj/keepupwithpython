class Greeter(object):
    def hello(self):
        print ("Hello")

    def goodbye(self):
        print ("good bye, c u nextime")

g = Greeter()
g.hello()







#
#
#
# #defining custom function more in details
# def starts_with_vowe(word):
#     return word[0] in "AEIOU"
# # starts_with_vowe()
#
# print starts_with_vowe("ERrd")
#
#
# names = ["Raj","Oioi","Test","Linda","Umber","Aed","kit","Eatt"]
#
# def filter_2_vowel(word_list):
#     vowel_words =[]
#     for word in word_list:
#         if starts_with_vowe(word):
#             vowel_words.append(word)
#     return vowel_words
#
#
# filter_2_vowel(names)
# print filter_2_vowel(names)
#






# # define custom function
# def rajthegreat ():
#     print ("Hi")
#
# rajthegreat()
#
#
# def rajthegreat1 (name):
#     print ("Hi " + name)
#
# rajthegreat1("jess")
#
# prices = [1.5,3.3,5.4,6.9]
# def sum(numbers):
#     total = 0
#     for number in numbers:
#         total = total + number
#     return total
#
# sum(prices)
# grocery_total = sum(prices)
# print ("grocery_total "   + str(grocery_total))
#
# prices = [1.5,3.3,5.4,6.9]
# total = 0
# for number in prices:
#     total = total + number
#
# print total

#
#
# # more of files practices
#
# import sys
# import random
#
# if len(sys.argv) < 2:
#     print ("Pls supply a flash card")
#     exit(1)
#
# flashcard_filename = sys.argv[1]
# # f = open("C:/Users/rgopalje/Desktop/writescore.txt","r")
# f = open(flashcard_filename,"r")
#
# question_dict ={}
#
# for line in f:
#     entry = line.strip().split(",")
#     question = entry[0]
#     answer = entry[1]
#     question_dict[question] = answer
#
# f.close()
#
# print ("Welcome to flashcard quitz")
# print ("at anytime, type quite to quite")
# print ("")
#
# questions = list(question_dict())
#
# while True:
#     question=random.choice(questions)
#     answer=question_dict[question]
#
#     print ("Question: " + question)
#     user_input = input("Your guess: ")
#     if user_input == "quit":
#         print ("thnx for playing game")
#         break
#     elif user_input == answer:
#         print ("Correct!")
#     else:
#         print ("sorry, the ans was: " + answer)
#






# # writing file from python
# f=open("C:/Users/rgopalje/Desktop/writescore.txt","w")
#
# while True:
#     party = input("partname > ")
#     if party == "quit":
#         break
#     score = input("score for" + party + ">")
#     f.write(party + "," + score + "\n")
# f.close()

# f=open("C:/Users/rgopalje/Desktop/writescore.txt","r")
# party1 ={}  #read from file and update the dictionary
#
# for line in f:
#     # print (line.strip().split(","))
#     # print (line.split(","))
#     entry = line.strip().split(",")
#     party2 = entry[0]
#     score1 = entry[1]
#     party1[party2] = score1
#     print (party2 + ": " + score1)
#
# f.close()
#
# f=open("C:/Users/rgopalje/Desktop/contrynames.txt",'r')
# def party1=("party","")
#
#  f.write()





# # reading from file and append field
# print "Open and reading from file and append field"
#
# countries=[]
#
# f=open("C:/Users/rgopalje/Desktop/contrynames.txt",'r')
# for line in f:
#     line=line.strip()
#     countries.append(line)
# f.close()
#
# print countries  # print filed countries
# print len(countries)   # how many countries
#
# country_r=[]
# country_p=[]
# country_a=[]
#
# # f=open("C:/Users/rgopalje/Desktop/contrynames.txt",'r')
# for country in countries:
#     if country[0]=='R':
#         country_r.append(country)
#         # print country
#         # print country_r
#     elif country[0]=='P':
#         # print countries
#         country_p.append(country)
#         # print country_p
#     else:
#         # print countries
#         country_a.append(country)
#         # print country_a
# # f.close()
#
# print country_r
# print country_p
# print country_a
#
# # # reading from file.
# # print "Open and reading from file and Print"
# # f=open("C:/Users/rgopalje/Desktop/contrynames.txt",'r')
# # for line in f:
# #     line=line.strip()
# #     print line
# # f.close()
#
#
#
#
#
#
#
#
#
### While Loops
# names =["Ryan","Raj","Val","Maya"]
# for i in names:
#     print ("Hello " + i)
#
# for i in [0,1,2,3,4]:
#     # print i
#     print ("Hello "+ str(i))
#
# counter = 0
# while counter < 5:
#     print ("While Hello " + str(counter))
#     counter = counter + 1
#  counter = 0
# while True:
#     print ("true Hello " + str(counter))
#     counter = counter + 1
#     if counter >=5:
#         break

#
# print "Break the While loop"
# while True:
#     user_input = input()
#     if user_input == 'quit':
#         print ("Good by break while loop!")
#         break
#     else:
#         print (user_input)
#

# #dictionary limit
# capdict={"il":"spring","ia":"demoines","test1":"test","test2":"f2test","test3":"f3test","test4":"f4test","ftest5":"f5test"}
# a=capdict
# print a
# print "^^^^^^^^^^^"
#
# import random
# states = list(capdict.keys())
# # print capdict1
# for i in [1,2,3]:
#     state=random.choice(states)
#     capital=capdict[state]
#     capguess=input("What is the capital of " + state + " ? ")
#
#     if capguess == capital:
#         print ("Correct! Nice Job.")
#     else:
#         print ("Incorrect. The capital of " + state + " is " + capital + " .")
# print ("All done")
#
# # # roll dice
# # print "Roll dice"
# # print '--------------'
# # import random
# # print type(random)
# # a=random.randint(1,6)
# # print ("your roll is:"+ str(a))
# #
# # cards=["jack","queen","king","ace"]
# # b=random.choice(cards)
# # print(cards)
# # print ("Raj\nthe\nGreat!")
# # # print("""this is to test to presever the indenting llllllll 'teste;
# # #              & * huhalkallh , 'at last' test!. """)
#
#
# # import matplotlib
# # c=matplotlib.use(4,5)
# # print c
#
#
#
#
#
#
# # # Dictionaries
# # icecream={"Alice":"Venila","bob":"stra","Cat":"chocla","test":"mint"}
# # print  icecream
# # print '*****'
# # print  icecream["Alice"]
# #
# # icecream["kate"]='rum raisin'
# #
# # print icecream["kate"]
# #
# # print icecream
# #
# # s="kate" in icecream
# # print s
# #
# # icecream["boo"]='Venila'
# # icecream["boo"]='Venila'
# # print icecream
# # type(icecream)
# # print type(icecream)
#
#
#
#
#
# # names = ["Alice","Bob","Cassie","Diane","Ellen","RajtheGreat!","Ink","ant","oil","linda"]
# # # #
# # # print (names)
# # # for aa in names:
# # #     print (aa)
# # #
# # # for word in names:
# # #     print("Hi " + word)
# # #
# # # name1 = "Alice"
# # # name1 [0]
# # # print name1[0]
# # # x=name1[0] in ["A","E", "I","O","U"]
# # # print x
# # # print (name1[0])
# # for xxx in names:
# #     if xxx[0] in "AEIOUaeiou":
# #         print ("name is star with vowels", xxx)
# # print '***************'
# #
# # vnames=[]
# # print vnames
# # print  names
# # print '&&&'
# # for yyy in names:
# #     if yyy[0] not in  "AEIOUaeiou":  #not a vowels
# #         vnames.append(yyy)
# #         print vnames
# #         print '####'
# # print vnames
# #
# # print '!!!!!!!'
# #
# # prices=[1.5,2.2,4.0,3,99.99,90]
# # total=0
# # counter=0
# # for zzz in prices:
# #     total=total+zzz
# #     # zzz + total = total
# #     print ("counter:", counter , ":" ,  total)
# #     counter=counter+1
# #     print
# # print '~~~~'
# # total=sum(prices)
# # print total