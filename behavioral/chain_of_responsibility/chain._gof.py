import abc


class Handler(abc.ABC):
    def __init__(self):
        self._successor = None

    def successor(self, successor):
        self._successor = successor

    @abc.abstractmethod
    def _can_handle(self, request):
        pass

    @abc.abstractmethod
    def _process_request(self, request):
        pass

    def handle(self, request):
        if self._can_handle(request):
            self._process_request(request)
        elif self._successor:
            self._successor.handle(request)



class ConcreteHandler1(Handler):
    def _can_handle(self, request):
        return 0 < request <= 10
    
    def _process_request(self, request):
        print('request {} handled in handler 1'.format(request))


class ConcreteHandler2(Handler):
    def _can_handle(self, request):
        return 10 < request <= 20
    
    def _process_request(self, request):
        print('request {} handled in handler 2'.format(request))

class ConcreteHandler3(Handler):
    def _can_handle(self, request):
        return 20 < request <= 30
    
    def _process_request(self, request):
        print('request {} handled in handler 3'.format(request))


class DefaultHandler(Handler):
    def _can_handle(self, request):
        return True
    
    def _process_request(self, request):        
        print('end of chain, no handler for {}'.format(request))


class Client:
    def __init__(self):
        h1 = ConcreteHandler1()
        h2 = ConcreteHandler2()
        h3 = ConcreteHandler3()
        h4 = DefaultHandler()

        h1.successor(h2)
        h2.successor(h3)
        h3.successor(h4)

        self.handlers = (h1, h2, h3, h4,)

    def delegate(self, requests):
        for request in requests:
            self.handlers[0].handle(request)


if __name__ == "__main__":
    client = Client()
    requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    client.delegate(requests)

### OUTPUT ###
# request 2 handled in handler 1
# request 5 handled in handler 1
# request 14 handled in handler 2
# request 22 handled in handler 3
# request 18 handled in handler 2
# request 3 handled in handler 1
# end of chain, no handler for 35
# request 27 handled in handler 3
# request 20 handled in handler 2
