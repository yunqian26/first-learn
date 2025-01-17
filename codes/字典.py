people={'first_name':'alex','last_name':'ben','age':18,'city':'guangzhou'}
print(people)

alpha={
    'print':'输出内容',
    'if':'判断语句',
    }

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

name=[]
for human in range(1,11):
    new_people={'性别':'male','身高':170}
    name.append(new_people)
print(name)
for k,v in alpha.items():
    print(k+' means: '+v+'\n')

for k in alpha.keys():
    print('what does'+k+' mean?\n')

for v in alpha.values():
    print('you can use '+v+'to do so\n')

print(people['first_name']+' like '+alpha['print']+'\n')

for name in sorted(favorite_languages.keys()):
    print(name.title()+' likes '+favorite_languages[name]+'\n')

cities={'beijing':{'country':'China','population':'1mol','fact':'The Great Wall'},'LA':{'country':'USA','population':'0.5mol','fact':'hollywood'},'Tokyo':{'country':'Japan','population':'0.2mol','fact':'FUJI mountain'}}
for city in cities:
    print(city.title()+' have '+cities[city]['population']+'people')