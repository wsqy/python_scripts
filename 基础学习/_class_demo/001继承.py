class KlsA():
    def hello(self, data):
        print("say KlsA...{}".format(data))


class KlsB(KlsA):
    pass


class KlsC(KlsA):
    def hello(self, data):
        print("say KlsC...{}".format(data))


class KlsD(KlsA):
    def hello(self, data):
        print("say KlsD...{}".format(data))
        KlsA.hello(self, data)


class KlsE(KlsA):
    def hello(self, data):
        print("say KlsD...{}".format(data))
        super(KlsE, self).hello(data)


class KlsF(KlsA):
    def hello(self, data):
        print("say KlsF...{}".format(data))
        super().hello(data)


if __name__ == "__main__":
    KlsF().hello('F')
