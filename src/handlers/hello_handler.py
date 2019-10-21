import hug


# @hug.get(examples='name=John')
# @hug.local()
# def hello_world(name: hug.types.text, hug_timer=3):
#     results = {
#         'message': f'Hello world, this is {name}!',
#         'took': float(hug_timer)
#     }
#     return results


# @hug.local()
# @hug.get(examples='')
# def hi():
#     return {'message': "Hey there"}


# @hug.local()
# @hug.get(examples='')
# def hi_person():
#     return {'message': "Hey there"}


# callable_app = __hug__.http.server()
# run(app=callable_app, reloader=True, port=8000)
