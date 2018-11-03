def student_info (*args, ** kwargs):
    print(args)
    print(kwargs)

#student_info('Math', 'Arts', name = 'John', age = 22)
#courses = ['Math', 'History', 'Arts']
info = {'name': 'John', 'age': 22, 'location': 'San Jose', 'courses': ['Math', 'History', 'Arts']}

student_info(**info)