class Application:
    def execute(self, request) -> None:
        print("In application!")

class InterceptorManager:
    def __init__(self, application) -> None:
        self.application = application
        self.interceptors = set()

    def add(self, interceptor):
        self.interceptors.add(interceptor)

    def remove(self, interceptor):
        self.interceptors.remove(interceptor)

    def execute(self, request):
        for interceptor in self.interceptors:
            interceptor.execute(request)
        self.application.execute(request)

class Interceptor:
    def execute(self, request):
        print("In interceptor!")

class AuthorizationInterceptor(Interceptor):
    def execute(self, request):
        print("In the authorization interceptor!")

class LoggingInterceptor(Interceptor):
    def execute(self, request):
        print("In the logging interceptor!")

class RandomInterceptor(Interceptor):
    def execute(self, request):
        print("In the random interceptor!")

interceptor_manager = InterceptorManager(Application())
logging_interceptor = LoggingInterceptor()
authorization_interceptor = AuthorizationInterceptor()
interceptor_manager.add(logging_interceptor)
interceptor_manager.add(authorization_interceptor)
interceptor_manager.execute("hola")