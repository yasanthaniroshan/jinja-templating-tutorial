from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader('templates'))
template = environment.get_template('profile_template.md')


user_details = [
    {'names':['John','Doe'],'date':11,'month':10,'year':2000},
    {'names':['Jane','Doe'],'date':12,'month':11,'year':2001},
    {'names':['Jack','Doe'],'date':13,'month':12,'year':2002},
    {'names':['Jill','Doe'], 'date':14,'month':1,'year':2003},
    {'names':['Joe','Doe'],'date':15,'month':2,'year':2004},
]


for user in user_details:
    with open(f'output/{user["names"][0]}.md', 'w') as f:
        f.write(template.render(
            names=user['names'],
            date=user['date'],
            month=user['month'],
            year=user['year']
        ))