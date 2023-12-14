from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader('code_snippets/variables/templates'))
template = environment.get_template('email_template.txt')

event_date = '2020-01-01'
event_time = '12:00:00'
event_platform = 'Zoom'
email_details = [
    {'name': 'John', 'email': 'john@sample.com'},
    {'name': 'Jane', 'email': 'jane@sample.com'},
    {'name': 'Joe', 'email': 'joe@sample.com'}
]

for detail in email_details:
    with open(f'code_snippets/variables/output/{detail["name"]}.txt', 'w') as f:
        f.write(template.render(
            name=detail['name'],
            event_date=event_date,
            event_time=event_time,
            event_platform=event_platform
        ))
    