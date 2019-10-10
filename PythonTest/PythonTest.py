# Dictionary Stuff
print("Hello World");
test = {'color':'green','points':5};

print(test['color']);
print(test['points']);

test['xPos'] = 0;
test['yPos'] = 25;
test['dummydata']='deleteme';
print(test);

del test['dummydata'];
print(test);

#===========================================
favLang = {'Chris':'C#','Hazel':'Plural Site','Bill':'VB','Larry':'dBase'};
print(favLang);

language = favLang['Chris'].title();
print(f"1 Favorite language is {language}.");
#===another way

language = favLang.get('Chris','Not assigned');
print(f"2 Favorite language is {language}.");

language = favLang.get('Christ','Not assigned');
print(f"3 Favorite language is {language}.");

#================= looping
for key, value in favLang.items():
    print(f"\nLanguage:{key} :: {value}");

for name in sorted(favLang.keys()):
    print(f"{name.title()}");

for langs in sorted(favLang.values()):
    print (f"{langs.title()}");

    #=========== 
while name != '':
    name = input("Enter name:")
    if (len(name)>0):
        print(f"Name entered is: {name}")

        age = input("Enter Age:")
        if (int(age) > 60):
            print("Dude your old!!")

    





