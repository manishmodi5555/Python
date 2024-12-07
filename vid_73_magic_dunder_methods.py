class a:
    name='ramesh'
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    #call methods
    def __call__(self, *args, **kwargs):
        return print(" hello buddy")

e=a()
print(e.name)
print(len(e))

# call methods
e()