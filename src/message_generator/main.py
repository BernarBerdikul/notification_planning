from jinja2 import Environment, FileSystemLoader, select_autoescape

# env = Environment(
#     loader=PackageLoader('message_generator', 'templates'),
#     autoescape=select_autoescape(['html'])
# )

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html']),
)


template = env.get_template('test.html')
html = template.render(first_name='Steve', my_list=[0, 2, 4, 6, 8])

print(html)
print(type(html))
