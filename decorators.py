def requiresAuthentication(postMethod):
    def wrapper(*args, **kwargs):
        # print('Wrapper is printing this line before the post method')
        if args[0] == True:
            postMethod(args[0])
        else:
            print('Authentication Failure')
    
    return wrapper
    
@requiresAuthentication
def postMethod(request):
    # do the operations
    print('The details are inserted in the database {0}'.format(request))

# decorator_return = requiresAuthentication(postMethod)
# decorator_return()

postMethod(True)